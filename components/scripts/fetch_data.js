// Fetches the html indexing from file and then returns a string with its content.
// If failed to load index, return a reject promise.
async function fetchAndFillIndexes() {
  // load the index from file and then add on the page
  try {
    result = await fetch("resources/data/indexes.txt");

    if (result.status == 200) {
      return await result.text();
    } else {
      throw new Error("Failed to load index");
    }
  } catch {
    return Promise.reject("Failed to load index");
  }
}

// Fetches latest 5 commits.
// If succesful, save to session storage at "commits". {message: "commit message", files: ["name.html", "name2.js", "name3.txt"]}.
// If failed to load commits, return a rejected promise.
async function fetchCommits() {
  try {
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

        // Fetches the specific commit to get the files that were edited
        // + ?.Date.now() to bust the cache and force the browser to reload the file.
        const result = await fetch(
          `https://api.github.com/repos/yasukawa426/yasukawa426.github.io/commits/${ref}`
        );

        if (result.status == 200) {
          // Success! Lets grab its files now!
          const commitJson = await result.json();
          let editedFiles = [];

          // For each file in the commit
          for (let i = 0; i < commitJson.files.length; i++) {
            // Remove its path and add to the array only the filename.
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
        } else {
          // Failed to fetch commit, throw.
          throw new Error();
        }
        sessionStorage.setItem("commits", JSON.stringify(commits));
      }
    } else {
      // Failed to load list of commits, throw.
      throw new Error();
    }
  } catch {
    // Something went wrong, clear commits key and reject the promise.
    sessionStorage.removeItem("commits");
    return Promise.reject("Failed to load commits :(");
  }
}

// Fetches my status from the status.json file and returns it.
// If failed to load status, return a rejected promise.
async function fetchStatus() {
  // load the status from file and then add on the page
  try {
    result = await fetch("resources/data/status.json" + "?" + Date.now());

    if (result.status == 200) {
      // Returns the object {status: "Feeling pretty proud of this app.", date: "today"}
      return JSON.parse(await result.text());
    } else {
      throw new Error("Failed to load status");
    }
  } catch {
    return Promise.reject("Failed to load status");
  }
}
