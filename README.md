# 🌩️ TYSONCLOUD-demo: Launch Your Database Mission!

## 🚀 Welcome to the Mission
Welcome! TYSONCLOUD-demo was used to teach game students at Neumont College of Computer Sceince the basics of PostgreSQL. All you need to do is sign up and create a database in 3 easy steps. 

🔗 **Live Demo**: [tysoncloud-demo.tysonjenkins.dev](https://tysoncloud-demo.tysonjenkins.dev/)

## 🌟 Why TYSONCLOUD-demo Rocks
- 🛠️ **Instant Postgres**: Spin up PostgreSQL databases faster than a speedrun world record.
- 🌐 **Remote Access**: Connect securely from anywhere using Cloudflare’s stealthy proxies.
- 🔒 **Authentication**: Basic authentication keeps your data secure while you build epic creations.

## 🧰 Requirements
- **Docker**: Your trusty container sidekick (version 20.10 or higher).
- **Cloudflared**: for secure, global access.
- **SQL Editor**: for managing your Postgres database

## 🚀 Accessing your Database
1. **Cloudflared Access**  
   ```bash
   cloudflared access tcp--hostname <hostname> --url localhost:5432
   ```

2. **Editing your Database**  
  depending on which method you use for accessing your database all settings should be the same:
   - hostname: localhost:5432
   - username: <username>
   - password: <password>

## 🤝 Join the TYSONCLOUD Crew
Want to make TYSONCLOUD-demo even more epic? Join the mission!
1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/your-cool-idea`.
3. Commit your brilliance: `git commit -m "Added cloud-tastic feature"`.
4. Push to the stars: `git push origin feature/your-cool-idea`.
5. Open a pull request and let’s shape the future!

## 🔮 What’s Next for the Mission
From Tinker Terrace, we’re plotting:
- 🗄️ Support for MySQL, MongoDB, and more databases.
- 🔐 OAuth2 for top-tier security.
- ⚡ Real-time monitoring with WebSocket magic.
- 💾 Auto-backups and scaling for unstoppable performance.

## 📜 License
MIT License
