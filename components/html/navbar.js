// NavBar component.
class NavBar extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = ` 
        <nav id="navbar">
        <ul>
            <li><a onclick="history.back()"><</a></li>
            <li><a href="/html">Home</a></li>
            <li></li>
          </ul>
        </nav>
    `;
  }
}

customElements.define("navbar-component", NavBar);
