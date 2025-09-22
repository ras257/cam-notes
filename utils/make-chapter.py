import os

MAIN_FILE = "main.tex"
CHAPTER_DIR = "chapters"

def get_dir_files(dir):
    return [name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]

def main():
    if not os.path.exists(MAIN_FILE):
        print("No main.tex found!")
        return

    if not os.path.exists("chapters"):
        print("No chapters folder!")
        return

    current_chapters = get_dir_files(CHAPTER_DIR)
    chapter_name = input("Enter chapter name (Leave blank to just regenerate subfile list): ")
    if chapter_name != "":
        chapter_name = chapter_name.replace(" ", "")
        new_chapter_file_name= f"{str(len(current_chapters) + 1)}-{chapter_name}.tex"
        new_chapter_path = os.path.join(CHAPTER_DIR, new_chapter_file_name)
        new_chapter_file = open(new_chapter_path, "w+") 
        new_chapter_file.close()
        current_chapters.append(new_chapter_file_name)
        print("New chapter created at " + new_chapter_path)
    
    main_file = open(MAIN_FILE, "r+")
    lines = main_file.readlines()
    start_line = lines.index("%%% START SUBFILES\n")
    end_line = lines.index("%%% END SUBFILES\n")
    chapter_subfile_lines = list(map(lambda name: f"\\subfile{{{CHAPTER_DIR}/{name}}}\n", current_chapters))

    new_file_lines = lines[:start_line + 1] + chapter_subfile_lines + lines[end_line:]
    main_file.seek(0)
    main_file.truncate(0)
    main_file.writelines(new_file_lines)
    main_file.close()
    print("Regenerated subfile list!")

main()
