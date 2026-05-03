# CorEvo Section 1 — Navigation Paths

## WebCT Menu Structure
- Top Menu:
  - Administration & Networking
  - Monitoring & Maintenance
  - Equipment
  - Interfaces
  - Services
  - Statistics

- Submenus located on left panel

---

## Paths

### Web Settings
Administration & Networking > Web Settings

### Network Element Information
Administration & Networking > Network Element Information

### System Settings
Administration & Networking > System Settings

### SNMP Settings
Administration & Networking > SNMP Settings

# ================================
# SECTION 2 — Navigation Paths
# ================================

### Networking Configuration
Administration & Networking > Networking Configuration

### Static Routing
Administration & Networking > Static Routing Configuration

### Protection Settings (Static LAG)
Equipment > Protection Settings

# ================================
# SECTION 3 — Navigation Paths
# ================================

### Alarm Management
Monitoring & Maintenance > Alarms Management (ASAP)

### Users Management
Administration & Networking > Users Management

# ================================
# SECTION 4 — Navigation Paths
# ================================

### Equipment Configuration
Equipment > Equipment Configuration

# ================================
# SECTION 5 — Navigation Paths
# ================================

### Port Configuration
Equipment > Port Configuration

### Ethernet Interfaces
Interfaces > Ethernet Interfaces

### Ethernet Services
Services > Ethernet Interface Services

### Radio Interfaces
Interfaces > Radio Interfaces

### Power Management
Equipment > Power Management

### Networking Configuration (PPP / OSPF)
Administration & Networking > Networking Configuration

### Radio Maintenance (PM)
Monitoring & Maintenance > Radio Maintenance

# ================================
# SECTION 6 — Navigation Paths
# ================================

### RLAG Configuration
Interfaces > Radio LAG Interface

### VLAN Management
Services > VLAN Management

# ================================
# SECTION 8 — Navigation Paths
# ================================

### Database Scratch
Monitoring & Maintenance > Debug Info

### Backup & Restore
Administration & Networking > Backup and Restore

# Alarm Retrieval Navigation

Retrieve active alarms:
Monitoring & Maintenance Domain > Active Alarms

Use Active Alarms before every clearing procedure.

General alarm-clearing workflow:
1. Retrieve all active alarms.
2. Review probable cause and friendly name/entity.
3. Decode affected rack, subrack, board, port, radio direction, channel, or LAG.
4. Identify whether alarm is SA, NSA, or abnormal condition.
5. Check for related alarms on the same path or entity.
6. Clear upstream/path/provisioning alarms first.
7. Re-retrieve Active Alarms.
8. Only replace hardware after provisioning, cabling, power, path, and related-alarm checks fail.