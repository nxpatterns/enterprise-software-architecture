import json

with open('local-modules/@nx/module-federation/package.json', 'r') as f:
    package_json = json.load(f)

package_json['dependencies']['webpack'] = '^5.89.0'  # Security fix version

with open('local-modules/@nx/module-federation/package.json', 'w') as f:
    json.dump(package_json, f, indent=2)

print("Updated webpack version in local @nx/module-federation package.json")
