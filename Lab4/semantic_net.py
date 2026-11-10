network = {
    'Student': {
        'is_a': 'Person',
        'has': ['RollNo', 'Name'],
        'takes': 'Course'
    },
    'Course': {
        'is_a': 'Subject',
        'has': 'Credits',
        'taught_by': 'Faculty'
    },
    'Faculty': {
        'is_a': 'Person',
        'teaches': 'Course'
    }
}

def show(node):
    if node in network:
        print(node)
        for rel, val in network[node].items():
            print("  ", rel, "->", val)
    else:
        print("not found")

show('Student')
print()
show('Course')
print()
show('Faculty')

# want to add Institute node later
