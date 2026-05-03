# Eclipse Node Installation Flow (Portal)

## New Installation — Full Workflow

1. Verify hardware installation is complete at both ends
2. Power on node and wait minimum 90 seconds before connecting
3. Connect to node using:
   - Ethernet (preferred if IP known)
   - DHCP (if no V.24 port)
   - V.24 (fallback)

4. Open Portal and connect to node

5. Verify licensing:
   Installation → Licensing

6. Configure node identity:
   Configuration → Information
   - Terminal name
   - Site name
   - Contact details
   - Site grid

7. Verify installed hardware:
   System Summary
   - Confirm plug-ins match installed modules
   - Accept/decline module types if required

8. Configure plug-ins:
   Configuration → Plug-Ins
   - Apply settings from datapack
   - REMOVE Tx Mute if set

9. Configure protection:
   Configuration → Protection

10. Configure circuits:
    Configuration → Circuits

11. Configure networking:
    Configuration → Networking
    - IP addressing
    - Routing
    - Trap destinations (if required)

12. Configure alarms (if required):
    Configuration → Alarm Actions

13. Set date and time:
    Configuration → Date/Time

14. Verify / update software:
    Configuration → Software Management

15. Configure security:
    Configuration → Security

16. Align antenna:
    - Use RSSI (ODU) OR
    - Diagnostics → Performance (RSL)

17. Repeat entire process on remote node

18. Validate link:
    - Compare RSL values vs datapack

19. Perform testing:
    - BER or RFC2544 test
    - Diagnostics → System/Controls

20. Generate report:
    Installation → As-Built Report

21. Capture commissioning data

→ Link is ready for service