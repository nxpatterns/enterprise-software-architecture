import json

with open('package.json', 'r') as f:
    package_json = json.load(f)

package_json['dependencies'][
    '@nx/module-federation'
] = 'file:local-modules/@nx/module-federation'  # security fix package

with open('package.json', 'w') as f:
    json.dump(package_json, f, indent=2)

print("Updated main package.json to use local @nx/module-federation")
