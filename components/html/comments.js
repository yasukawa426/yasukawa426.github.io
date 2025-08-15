// Comments component.
class Comments extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    // Creathe html structure for the comments section.
    this.innerHTML = ` 
        <div id="comments">
            <h1>Comments</h1>
            <p>
              PS:Comments are powered by GitHub Issues. After posting, remember
              to unsubscribe if you don't want to be notified of every new
              commment.
            </p>
        </div>
    `;

    // Load the utterances script and appendts it to the comments section.
    const script = document.createElement("script");
    script.src = "https://utteranc.es/client.js";
    script.setAttribute("repo", "yasukawa426/yasukawa426.github.io");
    script.setAttribute("issue-term", "title");
    script.setAttribute("label", "Comment");
    script.setAttribute("theme", "icy-dark");
    script.setAttribute("crossorigin", "anonymous");
    script.async = true;

    this.querySelector("#comments").appendChild(script);
  }
}

customElements.define("comments-section", Comments);
