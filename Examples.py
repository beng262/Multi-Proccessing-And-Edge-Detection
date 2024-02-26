import os
import multiprocessing

def search_file(file_path, keyword):
    with open(file_path, 'r') as file:
        contents = file.read()
        if keyword in contents:
            return True
    return False


def traverse_directory(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def parallel_file_search(directory, keyword):
    file_paths = traverse_directory(directory)
    pool = multiprocessing.Pool()  # Use default number of processes

    results = pool.map(lambda file_path: search_file(file_path, keyword), file_paths)

    # Collect the files where the keyword was found
    found_files = [file_paths[i] for i, result in enumerate(results) if result]

    # Display the results
    if found_files:
        print("Files found:")
        for file in found_files:
            print(file)
    else:
        print("No files found.")


if __name__ == '__main__':
    directory = input("Enter the directory path to search: ")
    keyword = input("Enter the keyword or phrase to search for: ")

    parallel_file_search(directory, keyword)

