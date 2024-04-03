---
marp: true
theme: default
class: 
  - lead
  - invert
---

# Dubai Linux Users' Group 1: Alpine Linux

Loïc Tosser
2024/04/03
![bg left:60%](https://www.netdata.cloud/img/alpine.svg)

---

![bg right:40%](https://secure.meetupstatic.com/photos/event/c/5/4/c/clean_519710508.webp)
# Introduction: Dubai Linux Users' Group

- Special thanks to Artur (all hail Artur)
- First Wednesday of every month
- Discussion first
- Hexagon ready for fights (hello Alaa)
- Exchanges about Linux and Open Source
- Windows is Haram!

---

# Small. Simple. Secure.

Alpine Linux is a security-oriented, lightweight Linux distribution.


![bg left](https://www.alpinelinux.org/banner.jpg)

---

![bg right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmczMTVmMjBpeHB2MzFpcDRtY2t1MzM2NmJxNDNpZHVxajFuMnlrbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o84U6421OOWegpQhq/giphy.gif)
# Alpine Linux: Innovation or Scam

How does Alpine Linux strengthen protection?
What benefits does Alpine's minimal footprint offer?
Is Alpine Linux a practical choice for production environments?

---

![bg fit right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzlhYnZlOTloN2YwbGpoOHphbm41ZjE1ZXVtMDNucnE0YzUyMGVvcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4Zgy9QqzWU8C3ugvCa/giphy.gif)

# Let's build a linux distribution

---

![bg left:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExanppd3NteWJsZ3RrY3h5ZHJwdTZoM2l0N3E0cGo1Nm05NDAyejBhciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J2iueH6VZQbkCmiHG1/giphy.gif)

# What do we need?

- Kernel
- LibC
- CoreUtils
- Init system
- Package manager

---

![bg](/alpine-linux/linux.jpeg)

---

![bg right:40%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTVoMTh0ODhncXZ3anBvN2puN2k3czZvaGhxcXZjdzdydWZveGlxaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jTMtoZKArEzNOTcyT0/giphy.gif)

| Elements   |      Ubuntu      |  Debian  |
|----------|:-------------:|:------:|
| Kernel |  Linux | Linux (but old)  |
| LibC  |    GLibC   |   GLibC (but old)  |
| CoreUtils | GNU |   GNU (but old)  |
| InitSystem | Systemd |    Systemd (but old)  |
| Package Manager | apt |   apt (but old)  |

Debian is just an old, outdated and unsecure Ubuntu!

---

![bg right:40%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWN6ZXM3ZzMyaTZkYzExaGVkeWJnMW5qbGt1YWU3MGxsZHFoN2UwdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VQDAVvvBgkT7NEfFGk/giphy.gif)

| Elements   |      Ubuntu      |  Fedora  |
|----------|:-------------:|:------:|
| Kernel |  Linux | Linux  |
| LibC  |    GLibC   |   GLibC  |
| CoreUtils | GNU |   GNU  |
| InitSystem | Systemd |    Systemd  |
| Package Manager | apt |   yum/dnf (rpm)  |

Ubuntu and Fedora are the same except for the package manager!

---
![bg right:40%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDlsbzB4aGd6bmpqZ3VybHBqbmx6Mjd5dTExYTRuaTE3cXluYjB4aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pPcRLX3R0AMK8sM63B/giphy.gif)

| Elements   |      Ubuntu      |  Alpine  |
|----------|:-------------:|:------:|
| Kernel |  Linux | Linux  |
| LibC  |    GLibC   |   Musl  |
| CoreUtils | GNU |   BusyBox  |
| InitSystem | Systemd |    OpenRC  |
| Package Manager | apt |   apk  |

Ubuntu and Alpine are different!

---

![bg  fit left:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWZuYXU1MXpxYTJ3aG92MWM3NjcyNWtvd2M4MDdtOTN6bmIxNncwZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fSYmbgG5Ug8S11K0FU/giphy.gif)

# The Cornerstone of Linux: libc

- libc, the standard C library, is crucial for system calls and basic functions in Linux.
- Multiple libc versions exist, such as glibc, musl, and uClibc, each with distinct advantages.
- Selecting a libc affects your system's performance, size, and compatibility with software.

---

![bg fit left:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnRudmx2aTNoYWYzbHpoZWRtcG14ajd4d3JuMWtocG9vcGh3dmQ3MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ornjIhZGFWpbcGMAU/giphy.gif)

# The choice of Alpine: Musl

- designed for simplicity, leading to a smaller, more efficient system footprint.
- Enhanced security through a clean codebase and proactive vulnerability patches.
- Strict adherence to standards ensures broad compatibility with software and languages.
- Reduce overall resource consumption.

---

![bg right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2FuemRrZmMwYmtoenFzeG95Mm5uMXh6NzFzNzJqcHY5YXkxeW55diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Jls16O6RdqyxueMvBj/giphy.gif)

# Is Musl Magic?

- May not compile/run due to musl's strict standards compliance (Hello JDK).
- Musl's developer and support community is smaller (changing)
- Lacks certain GNU extensions found in glibc

---

![bg fit left:50%](https://media.giphy.com/media/MJQJow1uUbNDy/giphy.gif)

# CoreUtils

- basic tools required for file, shell, and text management, pivotal for daily operations.
- GNU CoreUtils is part of the GNU project
- Alternatives are BusyBox and ToyBox

---

![bg right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDB3cTB3YTluNjV2OXo0amU3eTBrbG1hZndpaXFnNmxueTE1aXZieSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/c76IJLufpNwSULPk77/giphy.gif)

# Alpine <3 Busybox

- Combines tiny versions of UNIX utilities into a single small executable
- Optimized for simplicity and performance
- Fewer components and smaller size reduce the attack surface
- busybox = 792KB vs coreutils = 15.5MB

---

![bg fit left:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjlpYmdpeTVlYWg3eDdka3R5eGpvNjIyYXJyand5ZmVpd3B6MHo2NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ekMA4RKdSvROtoi3KB/giphy.gif)

# Is BusyBox magic?

Yes

---

![bg right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3M4Yzd0MXkxcGRnZGR6YjlrbGtkZW50ZzR2OXBjYnRsbGk2cnQxYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Wsva5clCvbxcbFURFm/giphy.gif)

# Init System

- SystemD won
- Awesome and Haram
- COVID-19

---

![bg fit left:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExODA4NTl5ZXgzMTJhbmtsNHVwa2FyamlmaW9tNzNyM2kyMnA3Z2FmeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vX9WcCiWwUF7G/giphy.gif)

# Why SystemD is bad?

- Complex
- not following UNIX principle
- Comes with a lot of stuff (network, DNS, user management, containers...)
- Lennart

---

![bg fit right:30%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmc0NmQ3aXJ3OXl0dzh2aXNpbjNyMWd0OXMxYnpsNnpjcmEweWJqcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cPKWZB2aaB3rO/giphy.gif)

# Why Alpine chose OpenRC?

- Emphasizes Unix philosophy with straightforward, easily customizable scripts.
- Flexible, modular management of services for tailored system control.
- Runs on various Unix-like systems, ensuring broad applicability.
- Less intrusive, allowing more user control and customization.
- Focuses on stability and efficiency, ideal for server environments.

---

![bg fit right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXB2aTh6ZjUyanJ6ZHl0bW1wazd1empxazFiZGNjNmdvMXZ2MnIxciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/afXo8c2BQVVi85brGj/giphy-downsized-large.gif)

# Package Managers: the holy war

- Haram: apt, rpm
- Halal: pacman, apk, emerge, paludis

---

![bg fit right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXp4eXFuczN5djQ2dzdrczg3dzVkcDdhNnpucWd6N2x5MTE1Znd4OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qLVGt6Go1dQFp4qVcg/giphy-downsized-large.gif)

# Is Alpine Used?

- Containers (-alpine)
- Router
- PostMarketOS
- Kalvad :-)

---

![bg fit right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXp4eXFuczN5djQ2dzdrczg3dzVkcDdhNnpucWd6N2x5MTE1Znd4OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qLVGt6Go1dQFp4qVcg/giphy-downsized-large.gif)

# Should you use Alpine?

Yes

---

![bg fit](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnhlNDJyMzNlMXM3Y2c0c3BseGxtNjh6M2tiYnl6cGd1ZWZmeGo1ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gd09Y2Ptu7gsiPVUrv/giphy.gif)

---

![bg fit right:50%](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTR3dDY3OHUzdXQ0d2t0YzY3aTB1cnh4bTMzYzd0YWZ5YnkyeTk0bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/usz0fqhUiVxSs6IUKB/giphy.gif)

# Use cases

- Containers
- Security (doas)
- Own packaging
- Network
- VMs
- Hosts

---

![bg fit left:30%](https://media.giphy.com/media/V0iBMLuftFImIBIGzV/giphy-downsized-large.gif)

# Conclusion

- Minimalist Design: "Maximizes efficiency, making it ideal for resource-constrained environments."
- Security-Focused: "Offers a reduced attack surface with musl libc and BusyBox."
- Resource Efficient: "Enhances performance by requiring less CPU and memory usage."
- User-Friendly: "Simplifies software management with the apk package system."
- Flexible Applications: "Versatile across servers, containers, and development environments."

---

![bg fit](https://media.giphy.com/media/d1E1YlkOTe4IfdNC/giphy.gif)
