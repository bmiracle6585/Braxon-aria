# Portal Connection Methods

## Ethernet (Primary)
- Preferred connection method
- Provides full network access
- Requires:
  - Matching subnet between PC and radio
  - Known IP address or auto-discovery

## DHCP Connection
- No manual IP required
- Radio assigns IP automatically
- Requirements:
  - DHCP enabled on radio
  - PC set to obtain IP automatically

## USB Connection
- Used when IP address is unknown
- Faster than V.24
- Local access only
- Default IP: 192.168.255.229
- Requires NCCv4 hardware

## V.24 Connection
- Used for initial access or recovery
- Local access only
- Default IP: 192.168.255.225
- Typically used when:
  - Auto-discovery fails
  - IP is unknown

## Connection Priority
1. Ethernet
2. DHCP
3. USB
4. V.24