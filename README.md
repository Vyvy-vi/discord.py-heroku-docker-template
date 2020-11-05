# discord.py-heroku-docker-template
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![built-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/Vyvy-vi/)
<p>
<a href="https://raw.githubusercontent.com/Vyvy-vi/TearDrops/main/LICENSE"><img src="https://img.shields.io/github/license/Py-Contributors/awesomeScripts?style=for-the-badge" alt="MIT license"></a>
<a href="https://discord.gg/invite"><img src="https://img.shields.io/discord/758030555005714512.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge" alt="discord invite"></a>

Template repository for making and deploying discord bots

## Hosting the bot locally:

- NOTE: To replicate this bot, you will need a bot **token**. Go get yours at https://discord.com/developers/ (If you need help with this step, feel free to ask for help in our [Support Server](https://discord.gg/invite)).
- Clone this repo using `git clone`
- cd into the bot folder.
- Add the token in a `.env` file in the project root as follows:
```text
DISCORD_BOT_TOKEN=<your token>
```
- Install [docker and docker-compose](https://docs.docker.com/desktop/) and then run:
```
docker-compose up
```
- Enjoy! (don't forget to add your own bot into your discord server by generating an invite link from the discord developers application page in [OAuth2 section](https://discord.com/developers/applications/) and choose application and check Oauth2 section)
- You may do bug-reporting or ask for help in on the SupportServer... or just open an issue on this repo.

## Requirements:
- python 3
- discord(rewrite branch)
- asyncio(inbuilt with python3.4)
- pymongo
- dnspython

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://allcontributors.org"><img src="https://avatars1.githubusercontent.com/u/46410174?v=4" width="100px;" alt=""/><br /><sub><b>All Contributors</b></sub></a><br /><a href="https://github.com/Vyvy-vi/discord.py-heroku-docker-template/commits?author=all-contributors" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Vyvy-vi"><img src="https://avatars0.githubusercontent.com/u/62864373?v=4" width="100px;" alt=""/><br /><sub><b>Vyom Jain</b></sub></a><br /><a href="#projectManagement-Vyvy-vi" title="Project Management">📆</a> <a href="#maintenance-Vyvy-vi" title="Maintenance">🚧</a> <a href="https://github.com/Vyvy-vi/discord.py-heroku-docker-template/commits?author=Vyvy-vi" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
