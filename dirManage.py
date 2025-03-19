import os

def list_mods():
    mods_list = [file for file in os.listdir("mods/") if file.endswith(".jar")]
    with open("mods.txt", "w") as f:
        f.write("\n".join(mods_list))

def update_mods(action):
    with open("mods.txt", "r") as f:
        mods = f.readlines()
    with open("mods.txt", "w") as f:
        for mod in mods:
            if action == "DEL":
                f.write("DEL " + mod)
            elif action == "DOWNLOAD":
                f.write("DOWNLOAD " + mod)
            else:
                print("Invalid action!")
                return
    print("Mods updated successfully!")

def main():
    while True:
        print("   _____                            _    _           _       _            ")
        print("  / ____|                          | |  | |         | |     | |           ")
        print(" | (___   ___ _ ____   _____ _ __  | |  | |_ __   __| | __ _| |_ ___ _ __ ")
        print("  \___ \ / _ \ '__\ \ / / _ \ '__| | |  | | '_ \ / _` |/ _` | __/ _ \ '__|")
        print(" |_____/ \___|_|    \_/ \___|_|     \____/| .__/ \__,_|\__,_|\__\___|_|   ")
        print("                                          | |                             ")
        print("                                          |_|                             ")
        print("\nMenu:")
        print("1. List mods")
        print("2. DEL")
        print("3. DOWNLOAD")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_mods()
        elif choice == "2":
            update_mods("DEL")
        elif choice == "3":
            update_mods("DOWNLOAD")
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
