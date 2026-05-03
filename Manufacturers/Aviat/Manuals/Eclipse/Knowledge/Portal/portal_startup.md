# Portal Startup and Connection Flow

## Startup Process
1. Connect PC to Eclipse radio
2. Launch Portal
3. Select target radio
4. Click Connect
5. Enter credentials (if required)
6. System Summary screen loads

## Connection Indicators

### Green Checkmark
- Radio detected on local network
- Does not guarantee connectivity

### No Response
- Likely IP mismatch or routing issue

### Timeout
- No communication path established

### Authentication Failure
- Incorrect username or password

## Auto-Discovery Behavior
- Portal sends a UDP broadcast
- Radios respond with:
  - IP address
  - Terminal name
- Detected radios appear in connection list

## Important Notes
- Ethernet should always be used when possible
- USB and V.24 are temporary access methods
- IP mismatch is the most common connection issue