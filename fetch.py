import os
import requests
import subprocess

if __name__ == "__main__":
    # Function to download a mod file
    def download_mod(mod_name, mod_download_url):
        mod_path = os.path.join('mods', mod_name)
        with open(mod_path, 'wb') as mod_file:
            mod_response = requests.get(mod_download_url)
            mod_file.write(mod_response.content)
        print(f"Downloaded mod: {mod_name}")

    # Function to delete a mod file
    def delete_mod(mod_name):
        mod_path = os.path.join('mods', mod_name)
        if os.path.exists(mod_path):
            os.remove(mod_path)
            print(f"Deleted mod: {mod_name}")
        else:
            print(f"Mod not found: {mod_name}")

    #Function to execute script
    def execute_mod(mod_name):
        basename, extension = os.path.splitext(mod_name)
        extension = extension[1:]
        if extension == 'py':
            subprocess.run(("python", mod_path))
        elif extension == 'js':
            subprocess.run(("node", mod_path))
        else:
            print("Invalid Script; Not Running")

    #Function to execute updates
    def execute_silent(mod_name):
        basename, extension = os.path.splitext(mod_name)
        extension = extension[1:]
        if extension == 'py':
            subprocess.Popen(("python", mod_path))
        elif extension == 'js':
            subprocess.Popen(("node", mod_path))
        else:
            return()


    # GitHub raw URL for mods.txt
    mods_txt_url = 'https://raw.githubusercontent.com/orixhusky/from-the-fog-modpack/main/mods.txt'

    # Fetch mods.txt content
    mods_txt_response = requests.get(mods_txt_url)
    if mods_txt_response.status_code == 200:
        mods_txt_content = mods_txt_response.text
        # Process mods.txt for custom commands and download specified mods
        for line in mods_txt_content.split('\n'):
            tokens = line.strip().split()
            if len(tokens) >= 2:
                command, mod_name = tokens[0], tokens[1]
                mod_path = os.path.join('mods', mod_name)
                if command == 'DOWNLOAD':
                    if not os.path.exists(mod_path):
                        print(f"Downloading mod: {mod_name}")
                        # Construct download URL for mod file
                        mod_download_url = f'https://raw.githubusercontent.com/orixhusky/from-the-fog-modpack/main/mods/{mod_name}'
                        download_mod(mod_name, mod_download_url)
                    else:
                        print(f"Mod {mod_name} already exists locally, skipping download")
                elif command == 'DEL':
                    if os.path.exists(mod_path):
                        print(f"Deleting mod: {mod_name}")
                        delete_mod(mod_name)
                    else:
                        print(f"Mod {mod_name} not found locally, skipping delete")
                elif command == 'EXEC':
                    execute_mod(mod_name)
                elif command == 'EXECSIL':
                    execute_silent(mod_name)
                else:
                    print(f"Unknown command: {command}")
            else:
                print('\n'"Finished Downloading Mods")
    else:
        print(f"Failed to fetch mods.txt from GitHub repository: {mods_txt_response.status_code}")

