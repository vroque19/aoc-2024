import sys
from collections import defaultdict

def isValid(rules_map, pages):
    seen = []
    for page in pages:
        seen.append(page)
        for num in seen:
            if page in rules_map:
                for rule in rules_map[page]:
                    if num == rule:
                        return False
    return True

def main(input):
    with open(input, 'r') as f:
        lines = f.readlines()
    
    # Split rules and updates
    idx = lines.index("\n")
    rules = lines[:idx]
    updates = lines[idx+1:]

    # Initialize rules_map
    rules_map = defaultdict(list)
    for line in rules:
        line = line.strip()
        pre, post = line.split('|')
        rules_map[pre].append(post)

    # Process updates and calculate result
    res = 0
    for pages in updates:
        if not pages.strip():
            continue  # Skip empty lines
        pages = [x.strip() for x in pages.split(',')]
        if isValid(rules_map, pages):
            mid = int(pages[len(pages) // 2])
            res += mid
    
    print(res)

if __name__ == "__main__":
    main(sys.argv[1])
