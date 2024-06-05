---
marp: true
theme: default
class: 
  - lead
  - invert
---

# Dubai Linux Users' Group 3: PyInfra

Loïc Tosser
2024/06/05
![bg fit right:60%](https://pyinfra.com/static/logo_readme.png)

---

![bg fit right:40%](https://secure.meetupstatic.com/photos/event/c/5/4/c/clean_519710508.webp)
# Introduction: Dubai Linux Users' Group

- Special thanks to Artur (all hail Artur)
- First Wednesday of every month
- Discussion first
- Hexagon ready for fights (hello Alaa)
- Exchanges about Linux and Open Source
- Windows is Haram!

---

# Infrastructure as Code (IaC)

**Definition:**
Infrastructure as Code (IaC) is the practice of managing and provisioning computing infrastructure through machine-readable configuration files, rather than through physical hardware configuration or interactive configuration tools.

---

# Infrastructure as Code (IaC)

**Benefits:**
- **Consistency:** Ensures that the same environment is deployed every time, reducing configuration drift.
- **Speed:** Automates infrastructure provisioning, reducing setup time.
- **Version Control:** Allows infrastructure configurations to be versioned and treated as code, enabling rollbacks and collaboration.
- **Scalability:** Simplifies scaling infrastructure up or down to meet demand.
- **Cost Efficiency:** Optimizes resource usage and reduces manual intervention, lowering operational costs.
- **Documentation:** Acts as documentation for the infrastructure setup, making it easier to understand and manage.

---

![bg fit right:60%](https://media.giphy.com/media/11tTNkNy1SdXGg/giphy.gif)
# It is Infrastructure as Code, not Infrastructure as YAML!

---

# Is that code?

```yaml
- name: systemd-timescynd config
  template:
    src: timesyncd.conf.j2
    dest: /etc/systemd/timesyncd.conf
  notify: restart systemd-timesyncd
```

---

# History of Tools

- **CFEngine:** First open-source tool.
- **Puppet:** Promoted declarative server management.
- **Pull vs. Push Methods:**
  - Pull: Server pulls configuration.
  - Push: Server pushes configuration.

---

# Declarative vs. Imperative

- **Declarative:** Define WHAT you want.
  - Used by Terraform, Puppet, Ansible.
- **Imperative:** Define HOW to do it.
  - Used by Chef, some Ansible and Salt support.

---

# Current Industry Tools

- **VMs and Servers:** Ansible (with AWX)
- **Infrastructure:** Terraform
- **Kubernetes:** Helm

---

# Issues with Ansible

- Custom inventories complexity.
- Managing state during execution.
- Scaling to thousands of servers.

---

# PyInfra to the Rescue!

- **Similarities with Ansible:**
  - Python-based.
  - Agentless.
  - Real-time debugging.
  - Two-stage process.
  - Declarative.

- **Advantages of PyInfra:**
  - Pure Python for inventory and roles.
  - Direct use of Python libraries like `requests`.

---

# Example: ZeroTier with PyInfra

```python
#Ansible

- name: Run the equivalent of "pacman -Sy" as a separate step
  community.general.pacman:
    update_cache: true

- name: Run the equivalent of "pacman -Su" as a separate step
  community.general.pacman:
    upgrade: true
    
#PyInfra

pacman.update()
pacman.upgrade()
```

---

# Example: ZeroTier with PyInfra

```python
import requests
from pyinfra.operations import apt, python, server

# Install ZeroTier
apt.packages(
    name='Install ZeroTier',
    packages=['zerotier-one'],
)

def authorize_server(state, host):
    status, stdout, stderr = host.run_shell_command('cat /var/lib/zerotier-one/identity.public')
    assert status is True

    server_id = stdout[0]
    response = requests.post('https://my.zerotier.com/.../{0}'.format(server_id))
    response.raise_for_status()

python.call(
    name='Authorize the server on ZeroTier',
    function=authorize_server,
)

server.shell(
    name='Execute some shell',
    commands=['echo "back to other operations!"'],
)
```

---

# Conclusion

- Moving from Ansible to PyInfra.
- Embracing Dev inside Ops.
- Highly recommend testing PyInfra, especially for Ansible fans!

---
![bg fit](https://media.giphy.com/media/d1E1YlkOTe4IfdNC/giphy.gif)