//TODO: Move any html to .html file using this function.
// Fetches the html indexing from file and then displays on the html.
async function fetchAndFillIndexes(indexesElement) {
  // load the index from file and then add on the page
  result = await fetch("indexes.txt");

  if (result.status == 200) {
    result.text().then((body) => {
      indexesElement.innerHTML = body;
    });
  } else {
    indexesElement.innerHTML = "<p>Failed to load index, sorry...</p>";
  }
}

// TODO: Fix not being able to load the commits from sessionStorage in the first time loading commits (from github).
// Fetches latest 5 commits.
// If succesful, save to session storage at "commits". ["latest commit message - files: ...", "second latest commit message", ...].
// If failed to load commits, throws an error.
async function fetchCommits() {
  result = await fetch(
    "https://api.github.com/repos/yasukawa426/yasukawa426.github.io/commits"
  );

  if (result.status == 200) {
    // Success!

    // List of jsons
    // {
    //  message: "",
    //  files: ["name", "name2", "name3"]
    // }
    let commits = [];

    let body = await result.json();

    // For the latest 5 commits,
    for (let i = 0; i < 5; i++) {
      // Get its message and sha.
      const message = body[i].commit.message;
      const ref = body[i].sha;

      // fetches the specific commit to get the files edited
      const result = await fetch(
        `https://api.github.com/repos/yasukawa426/yasukawa426.github.io/commits/${ref}`
      );

      if (result.status == 200) {
        // Success! Lets grab its files now!
        const commitJson = await result.json();
        let editedFiles = [];

        for (let i = 0; i < commitJson.files.length; i++) {
          // Split its path and add to the string
          if (commitJson.files[i].filename.includes("/")) {
            let fileName = commitJson.files[i].filename.split("/");

            editedFiles.push(fileName[fileName.length - 1].trim());
          } else {
            editedFiles.push(commitJson.files[i].filename.trim());
          }
        }

        // Then we add the commit with its message and files to the commits array.
        commits.push({
          message: message,
          files: editedFiles,
        });

        // commits.push(`${message} - Files: ${editedFiles.trim()}`);
      } else {
        throw new Error("Failed to load commits! :(");
      }
      sessionStorage.setItem("commits", JSON.stringify(commits));
    }
  } else {
    throw new Error("Failed to load commits! :(");
  }
}