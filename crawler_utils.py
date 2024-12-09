import os, subprocess

def generate_config(url):
    new_config = """
        import {{ Config }} from "./src/config";

        export const defaultConfig: Config = {{
        url: "{}",
        match: "{}**",
        exclude: "*://*/career*",
        maxPagesToCrawl: 50,
        outputFileName: "output.json",
        maxTokens: 200000000,
        }};
        """.format(url, url)

    with open("config.ts", 'w') as file:
        file.write(new_config)

def start_crawler(url):
    os.chdir("crawler")
    generate_config(url)
    command = "npm start"  
    subprocess.run(command, shell=True)