import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    
    # Get Names
    names = set(people) 
    
    # To begin, we have no prob
    final_prob = None
    
    # Let's go person by person and calculate their part of the prob
    for name in names:
        if people[name]['mother'] is None: # they have no parents
            # How many genes do they have?
            genes = get_genes(name, one_gene, two_genes)
            
            # Do they have the trait?
            trait = get_trait(name, has_trait)
            
            par_prob = PROBS['gene'][genes] * PROBS['trait'][genes][trait]
            
            # Calculate the "final_prob"
            final_prob = get_prob(final_prob, par_prob)
        
        else: # They do have parents
            kid_genes = get_genes(name, one_gene, two_genes)
            dad_genes = get_genes(people[name]['father'], one_gene, two_genes)
            mom_genes = get_genes(people[name]['mother'], one_gene, two_genes)
            
            kid_prob = get_parent_pass(kid_genes, dad_genes, mom_genes)
            
            kid_trait = get_trait(name, has_trait)
            kid_trait_prob = PROBS['trait'][kid_genes][kid_trait]
            
            kid_prob = kid_prob * kid_trait_prob
            
            final_prob = get_prob(final_prob, kid_prob)
            
    
    return final_prob
            
def get_parent_pass(kid_genes, dad_genes, mom_genes):
    
    dad_prob = pass_prob(dad_genes)
    mom_prob = pass_prob(mom_genes)
    
    # Need 2 genes passed - one from each parent
    if kid_genes == 2:
        prob = dad_prob * mom_prob
    elif kid_genes == 1:
        prob = dad_prob + mom_prob
    else:
        prob = (1 - dad_prob) * (1 - mom_prob)
    
    return prob
            
def pass_prob(genes):
    if genes == 2:
        prob = (1 - PROBS['mutation']) * (1 - PROBS['mutation'])
    elif genes == 2:
        prob = (1 - PROBS['mutation']) * (0 + PROBS['mutation'])
    else:
        prob = (0 + PROBS['mutation']) * (0 + PROBS['mutation'])
        
    return prob

def get_prob(final_prob, new_prob):
    if final_prob == None:
        final_prob = new_prob
    else:
        final_prob = final_prob * new_prob
    
    return final_prob

def get_trait(name, has_trait):
    if name in has_trait:
        trait = True
    else:
        trait = False
        
    return trait


def get_genes(name, one_gene, two_genes):
    if name in one_gene:
        genes = 1
    elif name in two_genes:
        genes = 2
    else:
        genes = 0
    
    return genes

def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    raise NotImplementedError


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
