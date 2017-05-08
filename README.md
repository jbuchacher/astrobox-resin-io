Astrobox 3D Printer Server, deployed using resin.io and Docker
=================

### https://dashboard.resin.io/apps/375145

**Resources:**

https://www.github.com/AstroPrint/AstroBox
https://www.github.com/resin-io/resin-wifi-connect
https://www.resin.io

**Building:**

- `bin/build`

**Running:**

- `bin/run`

**Deploying:**

-  Ensure you have the resin repository added as a remote: `git remote add resin joshb@git.resin.io:joshb/astrobox.git`
- `git push resin master`

**Configuration:**

- Stored in `config.yml`, which is symlinked to `/etc/astrobox/config.yml` in the running container
