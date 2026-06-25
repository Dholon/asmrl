# Advanced Smart Materials Research Laboratory (ASMRL) Center

**Digital Infrastructure & Public Portfolio** Department of Mathematics and Physical Sciences | Brac University  
[asmrl.org](https://asmrl.org)

---

## System Overview
This repository houses the front-end architecture for ASMRL. The platform highlights the laboratory's integrated methodology, bridging empirical materials synthesis with theoretical *ab initio* modeling via Density Functional Theory (DFT) and high-performance computing.

## Technical Architecture
The site utilizes a zero-build-step, single-file architectural pattern optimized for continuous edge deployment.

* **Core Structure:** HTML5
* **Styling Framework:** Tailwind CSS via Edge CDN
* **Iconography:** Lucide Icons via jsDelivr
* **Physics & Interactions:** Custom Vanilla JavaScript (ES6+) utilizing HTML5 `<canvas>` and scroll-mapped SVGs.

## Scientific Visualizations
The interface features mathematically grounded, interactive visualizations of computational condensed matter physics concepts.

* **Crystallographic Phase Transitions:** A 3D Canvas engine rendering fundamental space groups. Cursor proximity triggers real-time structural phase transitions (e.g., cubic to orthorhombic, or octahedral tilting) to simulate local thermodynamic perturbations.
* **Electronic Band Structure Mapping:** The Core Focus section features a scroll-driven SVG animation tracing a generic band structure plot across high-symmetry points ($\Gamma$, X, M) in the Brillouin zone.
* **Interactive Particle Network:** A global, antigravity-style Canvas layer simulating molecular dynamics and atomic attraction, rendering a subtle, interconnected network that reacts to cursor kinetic energy.

## Deployment Pipeline
The repository is configured for Continuous Integration/Continuous Deployment (CI/CD) via Netlify.

* **Trigger:** Pushes to the `main` branch automatically execute a Netlify webhook.
* **Distribution:** The raw `index.html` is compiled and distributed globally via the Netlify Content Delivery Network.
* **Routing:** Direct resolution to the `asmrl.org` domain.

## Content Management Operations

* **Image Assets:** Upload new infrastructure or synthesis photos to the `images/` directory. Update the respective `<img src="images/filename.extension">` tags within the slider containers.
* **Lab Momentum:** Locate the `news-slider-container` element. Update the text within the `<span>` (Date), `<h4>` (Headline), and `<p>` (Description) blocks to announce new publications, thesis defense milestones, or new HPC hardware acquisitions.
* **Physics Engine Parameters:** Modify variables such as `numCrystals`, `exclusionRadius`, and `targetMultiplier` within the `<script>` block to fine-tune the density, repulsion zones, and cursor acceleration vectors of the background nodes.

## Academic Integrity & Contact
This source code is proprietary to the ASMRL research group led by Md. Firoze H. Haque, PhD, Associate Professor.

Direct inquiries regarding machine learning applications in DFT, material synthesis collaboration, or M.Sc./Undergraduate recruitment to the Principal Investigator or the designated Research Assistant, Dholon Kumar Paul.
