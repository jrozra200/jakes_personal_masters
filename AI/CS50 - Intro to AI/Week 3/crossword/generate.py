import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for domain in self.domains:
            length = domain.length
            for word in self.domains[domain].copy():
                if len(word) != length:
                    self.domains[domain].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        overlap = self.crossword.overlaps[x, y]
        revision = False
        
        if overlap is None:
            return revision
        
        for x_word in self.domains[x].copy():
            x_count = 0
            for y_word in self.domains[y]:
                if x_word[overlap[0]] == y_word[overlap[1]]:
                    x_count += 1
            
            if x_count == 0:
                self.domains[x].remove(x_word)
                revision = True
        
        return revision

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            queue = list(self.crossword.overlaps.keys())
        else:
            queue = arcs
        
        while(len(queue) > 0):
            x, y = queue[0]
            queue.remove((x, y))
            
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
            for n in self.crossword.neighbors(x):
                if n != y:
                    queue.append((n, x))
        
        return True
        

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        
        # If there is not an assignment for every variable, it is not complete
        if len(assignment) != len(self.domains):
            return False
        else:
            # For every assignment, let's make sure the variable is in the
            # crossword set of variables AND there is only one word assigned
            for ass in assignment:
                if ass not in self.domains or assignment[ass] not in self.domains[ass]:
                    return False
        
        return True
            

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        
        # An assignment is consistent if it satisfies all of the constraints of 
        # the problem: that is to say, all values are distinct, every value is 
        # the correct length, and there are no conflicts between neighboring 
        # variables.
        
        unique_values = set()
        
        for ass in assignment:
            value = assignment[ass]
            
            # if this value has already been used, not every value is distinct
            if value in unique_values: 
                return False
            
            # add it to the running list of unique values
            unique_values.add(value) 
            
            # if the variable is not the right length, the assignment is bad
            if len(value) != ass.length:
                return False
            
            # check for conflicts in the neighbors
            for overlap in self.crossword.overlaps:
                x, y = overlap
                
                # We are only checking for ass right now
                if x == ass:
                    
                    # What is the intersection point?
                    intersection = self.crossword.overlaps[(x, y)]
                    
                    # if intersection is none, then we move on
                    # Also, we may have an incomplete solution. If y is in assignment, 
                    # let's check it. Otherwise, let's move on
                    if intersection is not None and y in assignment.keys():
                        other_value = assignment[y]
                        
                        # make sure there are no conflicts among neighbors
                        if value[intersection[0]] != other_value[intersection[1]]:
                            return False
            
        # if you get through that shenanigans, then you are good
        return True


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # Get the whole set of variables
        all_values = set(self.domains)
        all_values.remove(var)
        for ass in assignment:
            if ass in all_values:
                all_values.remove(ass)
        
        track = {}    
        for word in self.domains[var]:
            # So far, we've ruled out 0 neighboring unassigned variables
            ruled_out = 0
            for val in all_values:
                # if they overlap, let's check it out
                if self.crossword.overlaps[(var, val)] != None:
                    intersection = self.crossword.overlaps[(var, val)]
                    
                    # for each word in the intersecting domain, let's make sure 
                    # the letters line up. If they don't we've ruled something out
                    for other_word in self.domains[val]:
                        if word[intersection[0]] != other_word[intersection[1]]:
                            ruled_out += 1
            
            # Add this word to the dictionary with the number ruled out
            track[word] = ruled_out
        
        # return the sorted list of keys                    
        return sorted(track, key = track.get)
        

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Get the whole set of variables
        all_values = set(self.domains)
        
        # Remove the variables that are already assigned
        for ass in assignment:
            if ass in all_values:
                all_values.remove(ass)
        
        track = [] 
        for val in all_values:
            domains = len(self.domains[val])
            degree = len(self.crossword.neighbors(val))
            
            track.append((val, domains, degree))
        
        # First sort track by least remaining values in its domain
        track = sorted(track, key = lambda x: x[1])
        lowest = track[0][1]
        new_track = []
        for t in track:
            if t[1] == lowest:
                new_track.append(t)
        
        new_new_track = sorted(new_track, key = lambda x: -x[2])
        # return the value with the least remaining values in its domain and 
        # highest degree
        return new_new_track[0][0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        
        var = self.select_unassigned_variable(assignment)
        
        for val in self.order_domain_values(var, assignment):
            new_assignment = assignment
            new_assignment[var] = val
            if self.consistent(new_assignment):
                assignment[var] = val
                result = self.backtrack(assignment)
                
                if result is not None:
                    return result
                assignment.pop(var)
        
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
