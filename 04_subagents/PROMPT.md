Let's build a hotel room booking app for Seroter Hotels consisting of a Go backend API and a web frontend. 
 
First, launch the **Engineering Manager** agent to design the API and frontend, saving the design and a Mermaid diagram into an artifact called 'architecture.md'. 
 
Once the design is ready, launch three agents in parallel:
1. **Test Manager**: Write a simple API test plan and append it to 'architecture.md'.
2. **Backend Engineer**: Build a clean Go REST API with standard error handling based on the design.
3. **Frontend Engineer**: Build a responsive web UI using a simple CSS framework like Tailwind to interact with the API (skip UI testing).
 
As soon as the Test Manager finishes the plan, have them hand it off to the Backend Engineer, who reads the plan from 'architecture.md' and adds the Go tests to the code. After both engineers finish building, the Test Manager runs the tests. Finally, spin up both components and a browser so I can test the live app.
