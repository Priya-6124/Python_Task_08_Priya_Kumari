import os
import shutil
import csv
from datetime import datetime
from collections import defaultdict
import time


class SmartFileOrganizer:

    IMAGE_EXTENSIONS = {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"
    }

    DOCUMENT_EXTENSIONS = {
        ".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx",
        ".xls", ".xlsx", ".csv", ".odt"
    }

    VIDEO_EXTENSIONS = {
        ".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"
    }

    AUDIO_EXTENSIONS = {
        ".mp3", ".wav", ".aac", ".ogg", ".flac"
    }

    ARCHIVE_EXTENSIONS = {
        ".zip", ".rar", ".7z", ".tar", ".gz"
    }

    PROGRAM_EXTENSIONS = {
        ".exe", ".msi", ".apk", ".py", ".java", ".cpp",
        ".c", ".html", ".css", ".js"
    }

    def __init__(self, folder):
        self.folder = folder
        self.files = []
        self.categories = defaultdict(list)
        self.duplicates = []
        self.category_count = defaultdict(int)

    # -----------------------------------------------------

    def validate_directory(self):
        if not os.path.exists(self.folder):
            raise FileNotFoundError("Folder does not exist.")

        if not os.path.isdir(self.folder):
            raise NotADirectoryError("Invalid directory.")

    # -----------------------------------------------------

    def scan_files(self):

        self.files.clear()

        print("\nScanning Files...\n")

        for item in os.listdir(self.folder):
            full_path = os.path.join(self.folder, item)

            if os.path.isfile(full_path):
                self.files.append(full_path)

        print("=" * 60)
        print("FILES FOUND")
        print("=" * 60)

        for file in self.files:
            name = os.path.basename(file)
            ext = os.path.splitext(file)[1]

            print(f"{name:<40} {ext}")

        print("\nTotal Files :", len(self.files))

    # -----------------------------------------------------

    def get_category(self, extension):

        extension = extension.lower()

        if extension in self.IMAGE_EXTENSIONS:
            return "Images"

        elif extension in self.DOCUMENT_EXTENSIONS:
            return "Documents"

        elif extension in self.VIDEO_EXTENSIONS:
            return "Videos"

        elif extension in self.AUDIO_EXTENSIONS:
            return "Audio"

        elif extension in self.ARCHIVE_EXTENSIONS:
            return "Archives"

        elif extension in self.PROGRAM_EXTENSIONS:
            return "Programs"

        else:
            return "Others"

    # -----------------------------------------------------

    def organize_files(self):

        print("\nOrganizing Files...\n")

        total = len(self.files)

        for index, file in enumerate(self.files):

            extension = os.path.splitext(file)[1]
            category = self.get_category(extension)

            destination_folder = os.path.join(self.folder, category)

            os.makedirs(destination_folder, exist_ok=True)

            filename = os.path.basename(file)

            destination = os.path.join(destination_folder, filename)

            counter = 1

            while os.path.exists(destination):

                name, ext = os.path.splitext(filename)

                destination = os.path.join(
                    destination_folder,
                    f"{name}_{counter}{ext}"
                )

                counter += 1

            shutil.move(file, destination)

            self.categories[category].append(destination)
            self.category_count[category] += 1

            self.progress(index + 1, total)

        print("\n\nOrganization Complete!")

    # -----------------------------------------------------

    def progress(self, current, total):

        length = 40

        percent = current / total

        filled = int(length * percent)

        bar = "█" * filled + "-" * (length - filled)

        print(
            f"\r[{bar}] {int(percent*100)}%",
            end=""
        )

        time.sleep(0.05)

    # -----------------------------------------------------

    def statistics(self):

        print("\n")

        print("=" * 60)
        print("FILE STATISTICS")
        print("=" * 60)

        print("{:<20}{}".format("Category", "Count"))
        print("-" * 35)

        total = 0

        for category in [
            "Images",
            "Documents",
            "Videos",
            "Audio",
            "Archives",
            "Programs",
            "Others"
        ]:

            count = self.category_count.get(category, 0)

            print("{:<20}{}".format(category, count))

            total += count

        print("-" * 35)

        print("{:<20}{}".format("Total Files", total))

    # -----------------------------------------------------

    def search_name(self):

        keyword = input("\nEnter file name: ").lower()

        found = False

        print()

        for root, dirs, files in os.walk(self.folder):

            for file in files:

                if keyword in file.lower():
                    print(os.path.join(root, file))
                    found = True

        if not found:
            print("No files found.")

    # -----------------------------------------------------

    def search_extension(self):

        extension = input("Enter extension (.pdf): ").lower()

        found = False

        print()

        for root, dirs, files in os.walk(self.folder):

            for file in files:

                if file.lower().endswith(extension):
                    print(os.path.join(root, file))
                    found = True

        if not found:
            print("No matching files.")

    # -----------------------------------------------------

    def duplicate_detection(self):

        names = defaultdict(list)

        for root, dirs, files in os.walk(self.folder):

            for file in files:
                names[file].append(os.path.join(root, file))

        self.duplicates.clear()

        for file, paths in names.items():

            if len(paths) > 1:
                self.duplicates.append((file, paths))

        print("\nDuplicate Files")

        if not self.duplicates:

            print("No Duplicate Files Found")

        else:

            for file, paths in self.duplicates:

                print("\n", file)

                for p in paths:
                    print(" ", p)

    # -----------------------------------------------------

    def largest_file(self):

        largest = None
        size = 0

        for root, dirs, files in os.walk(self.folder):

            for file in files:

                path = os.path.join(root, file)

                file_size = os.path.getsize(path)

                if file_size > size:

                    size = file_size
                    largest = path

        print("\nLargest File")

        print(largest)

        print(round(size / (1024 * 1024), 2), "MB")

    # -----------------------------------------------------

    def recently_modified(self):

        print("\nRecently Modified Files\n")

        recent = []

        for root, dirs, files in os.walk(self.folder):

            for file in files:

                path = os.path.join(root, file)

                recent.append(
                    (
                        os.path.getmtime(path),
                        path
                    )
                )

        recent.sort(reverse=True)

        for item in recent[:10]:

            print(
                datetime.fromtimestamp(item[0]),
                os.path.basename(item[1])
            )

    # -----------------------------------------------------

    def empty_folders(self):

        print("\nEmpty Folders")

        found = False

        for root, dirs, files in os.walk(self.folder):

            if not dirs and not files:
                print(root)
                found = True

        if not found:
            print("No Empty Folders")

    # -----------------------------------------------------

    def delete_empty_folders(self):

        deleted = 0

        for root, dirs, files in os.walk(
                self.folder,
                topdown=False):

            if not dirs and not files:

                if root != self.folder:

                    os.rmdir(root)

                    deleted += 1

        print("\nDeleted", deleted, "Empty Folders")

    # -----------------------------------------------------

    def csv_report(self):

        file = os.path.join(self.folder, "report.csv")

        with open(file, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(["Category", "Count"])

            for category, count in self.category_count.items():

                writer.writerow([category, count])

        print("\nCSV Report Generated.")

    # -----------------------------------------------------

    def text_report(self):

        report = os.path.join(
            self.folder,
            "file_report.txt"
        )

        with open(report, "w") as f:

            f.write("=" * 60 + "\n")
            f.write("SMART FILE ORGANIZER REPORT\n")
            f.write("=" * 60 + "\n\n")

            f.write("Generated : ")
            f.write(str(datetime.now()))
            f.write("\n\n")

            f.write("Folder : ")
            f.write(self.folder)
            f.write("\n\n")

            f.write("Category Counts\n")

            for category, count in self.category_count.items():

                f.write(f"{category} : {count}\n")

            f.write("\nDuplicate Files\n")

            if not self.duplicates:

                f.write("No Duplicate Files\n")

            else:

                for file, paths in self.duplicates:

                    f.write(file + "\n")

                    for p in paths:
                        f.write("   " + p + "\n")

            f.write("\nFolder Structure\n")

            for root, dirs, files in os.walk(self.folder):

                level = root.replace(self.folder, "").count(os.sep)

                indent = " " * 4 * level

                f.write(indent + os.path.basename(root) + "\n")

                for file in files:

                    f.write(
                        indent + "    " + file + "\n"
                    )

        print("\nText Report Generated.")

    # -----------------------------------------------------

    def menu(self):

        while True:

            print("\n")

            print("=" * 60)
            print("SMART FILE ORGANIZER")
            print("=" * 60)

            print("1. Scan Files")
            print("2. Organize Files")
            print("3. Statistics")
            print("4. Search by Name")
            print("5. Search by Extension")
            print("6. Duplicate Detection")
            print("7. Largest File")
            print("8. Recently Modified Files")
            print("9. Empty Folder Detection")
            print("10. Delete Empty Folders")
            print("11. Export CSV Report")
            print("12. Generate Text Report")
            print("13. Exit")

            choice = input("\nEnter Choice : ")

            if choice == "1":
                self.scan_files()

            elif choice == "2":
                self.organize_files()

            elif choice == "3":
                self.statistics()

            elif choice == "4":
                self.search_name()

            elif choice == "5":
                self.search_extension()

            elif choice == "6":
                self.duplicate_detection()

            elif choice == "7":
                self.largest_file()

            elif choice == "8":
                self.recently_modified()

            elif choice == "9":
                self.empty_folders()

            elif choice == "10":
                self.delete_empty_folders()

            elif choice == "11":
                self.csv_report()

            elif choice == "12":
                self.text_report()

            elif choice == "13":
                print("\nThank You")
                break

            else:
                print("Invalid Choice")


# -----------------------------------------------------

def main():

    print("=" * 60)
    print("SMART FILE ORGANIZER")
    print("=" * 60)

    folder = input("\nEnter Folder Path : ")

    try:

        organizer = SmartFileOrganizer(folder)

        organizer.validate_directory()

        organizer.menu()

    except PermissionError:
        print("Permission Denied.")

    except FileNotFoundError as e:
        print(e)

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    main()