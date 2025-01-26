import json

try:
    with open('apps/fe-base/project.json', 'r') as f:
        project_json = json.load(f)

    # Remove any webpack-related configurations
    if 'targets' in project_json:
        for target in project_json['targets'].values():
            if 'executor' in target:
                if '@nx/webpack:webpack' in target['executor']:
                    target['executor'] = '@angular-devkit/build-angular:browser'
                elif '@nx/webpack:dev-server' in target['executor']:
                    target['executor'] = '@angular-devkit/build-angular:dev-server'

    with open('apps/fe-base/project.json', 'w') as f:
        json.dump(project_json, f, indent=2)

    print("apps/fe-base/project.json updated successfully.")
except FileNotFoundError:
    print("apps/fe-base/project.json not found. Skipping.")
