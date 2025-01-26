import json

# Removes webpack-related packages from package.json

with open('package.json', 'r') as f:
    package_json = json.load(f)

webpack_related = ['webpack', 'webpack-cli', '@nx/webpack', '@nx/module-federation']

for section in ['dependencies', 'devDependencies']:
    if section in package_json:
        package_json[section] = {
            k: v
            for k, v in package_json[section].items()
            if not any(wp in k for wp in webpack_related)
        }

with open('package.json', 'w') as f:
    json.dump(package_json, f, indent=2)

print("Webpack-related packages removed from package.json")
