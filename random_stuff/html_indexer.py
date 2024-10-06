import os
# I'm gonna make a dictionari to represent the folders, if it doesnt end in .*, its a folder and I should look for the children:

# tree = {
#     "title": "root",
#     "child": [
#         {
#             "title": "html",
#             "child": [
#                 {"title": "about_me"},
#                 {
#                     "title": "dream_journal",
#                     "child": [
#                         {
#                             "title": "dream_journal.html",
#                             "child": "",
#                         },
#                         {
#                             "title:": "dreams",
#                             "child": ["..."],
#                         },
#                     ],
#                 },
#             ],
#         },
#         {
#             "title": "random_pages",
#             "child": "...",
#         },
#         {
#             "title": "templates",
#             "child": "...",
#         },
#     ],
# }


HTML_PATH = "./html"

# def listAllSubDirs()


# Get a list of folders names string  (['dream_journal', 'random_pages', 'templates'])
# folders = os.walk(HTML_PATH)
i = 0
for root, dirs, files in os.walk(HTML_PATH):
    print("Iteration " + str(i) + ":")
    print("root:" + str(root))
    print("dir: " + str(dirs))
    print("file:" + str(files))
    i += 1


# for path in folders:
#     # if is a folder
#     if not path.endswith(".html"):
#         print("Is a folder: " + path)

#     # if is a file
#     else:
#         print("Is a file: " + path)
