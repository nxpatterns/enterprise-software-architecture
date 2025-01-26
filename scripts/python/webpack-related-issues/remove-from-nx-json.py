import json

try:
    with open('nx.json', 'r') as f:
        nx_json = json.load(f)

    # Remove any webpack-related configurations
    if 'plugins' in nx_json:
        nx_json['plugins'] = [p for p in nx_json['plugins'] if 'webpack' not in p]

    if 'tasksRunnerOptions' in nx_json:
        if 'default' in nx_json['tasksRunnerOptions']:
            if 'options' in nx_json['tasksRunnerOptions']['default']:
                if (
                    'runtimeCacheInputs'
                    in nx_json['tasksRunnerOptions']['default']['options']
                ):
                    nx_json['tasksRunnerOptions']['default']['options'][
                        'runtimeCacheInputs'
                    ] = [
                        i
                        for i in nx_json['tasksRunnerOptions']['default']['options'][
                            'runtimeCacheInputs'
                        ]
                        if 'webpack' not in i
                    ]

    with open('nx.json', 'w') as f:
        json.dump(nx_json, f, indent=2)

    print("nx.json updated successfully.")
except FileNotFoundError:
    print("nx.json not found. Skipping.")
