// NavBar component.
class NavBar extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = ` 
        <nav id="navbar">
          <ul>
            <li><a href="/">Home</a></li>
          </ul>
        </nav>
    `;
  }
}

customElements.define("navbar-component", NavBar);
