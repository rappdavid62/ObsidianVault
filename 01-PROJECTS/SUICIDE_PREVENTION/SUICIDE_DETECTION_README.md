# Polaris Enhanced Safety System
## Suicide Decision Detection & Crisis Integration

**State Not Fate - Depression Recovery Operating System**
Last Updated: June 2026

---

## Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Architecture](#architecture)
4. [How It Works](#how-it-works)
5. [For Users](#for-users)
6. [For Clinicians](#for-clinicians)
7. [For Developers](#for-developers)
8. [Ethical Framework](#ethical-framework)
9. [Quick Start](#quick-start)

---

## Overview

The Polaris Enhanced Safety System integrates three critical layers of suicide decision detection and crisis intervention directly into the State Not Fate daily anchor system.

**This is NOT:**
- A replacement for professional mental health care
- A diagnostic tool
- Able to guarantee safety
- Appropriate for managing active attempts

**This IS:**
- An early warning system for people using Polaris
- A tool to help people recognize concerning patterns
- A bridge to crisis resources and professional help
- Integrated into daily anchors for maximum accessibility

---

## Key Features

### 1. **Three-Tier Safety Screening**

**Tier 1: Quick Daily Check (2 questions)**
- Integrated into daily energy check-in
- 1 minute to complete
- Non-intrusive, normalizing language
- Triggers expanded assessment if concerning

**Tier 2: Intent vs. Ideation Differentiation (4 questions)**
- Determines whether thoughts are passive or active
- Assesses access to means
- Evaluates timeline
- Identifies protective factors

**Tier 3: Comprehensive Risk Assessment**
- Detailed behavioral changes
- Access to means evaluation
- Protective factors inventory
- Contextual risk factors

### 2. **Pattern Detection Algorithm**

Passive monitoring that flags concerning patterns:
- Rapid energy collapse after stability
- Anchor abandonment (was doing anchors, suddenly stops)
- Accumulation of zero-days (5+ days with no anchor completion)
- Social isolation spike
- Combined low hope + loss of meaning
- Rumination escape (stopped using thought corrections)

### 3. **Adaptive Risk Levels**

```
🟢 LOW: Stable monitoring
🟡 LOW-MODERATE: Enhanced oversight
🟠 MODERATE: Safety planning initiated
🔴 ELEVATED: Active crisis protocol
🚨 ACUTE: Emergency response
```

### 4. **Escalation Protocols**

- **Level 3 (Emergency)**: Immediate crisis hotline, 911, emergency contacts
- **Level 2 (Active Crisis)**: Crisis protocol, daily check-ins, enhanced monitoring
- **Level 1 (Safety Alert)**: Collaborative safety planning, increased contact
- **Level 0 (Normal)**: Standard monitoring

### 5. **Crisis Safe Box**

Pre-loaded with:
- Location-specific crisis resources
- Safe contact information
- Reasons to live
- Distractions list
- Grounding techniques with instructions
- De-escalation methods
- Emergency hotlines

### 6. **Adaptive Anchors**

Based on risk level, anchors automatically adjust:
- **Low risk**: Continue standard anchors
- **Moderate risk**: Add connection anchors, daily reasons review
- **Elevated risk**: Survival-only mode, hourly check-ins
- **Acute risk**: Emergency anchors only

---

## Architecture

### Module Structure

```
src/
├── safety-detection.js          # Core screening and assessment
├── crisis-protocol.js           # Crisis response pathways
├── polaris-safety-integration.js # Connection to daily system
├── ethical-guidelines.js        # Principles and boundaries
└── implementation-guide.js      # Setup and testing
```

### Data Flow

```
Daily Check-In
    ↓
Quick Ideation Question (Tier 1)
    ↓
[If concerning: Trigger Tier 2]
    ↓
[If persistent concern: Offer Tier 3]
    ↓
Risk Score Calculation
    ↓
Pattern Detection
    ↓
Risk Level Assignment
    ↓
Adaptive Response
    ├─ Modify anchors
    ├─ Display safety dashboard
    ├─ Offer crisis resources
    └─ Schedule next assessment
```

---

## How It Works

### Daily Workflow

1. **User opens Polaris, starts daily check-in**
   - Energy level selection
   - Mood check
   - **NEW: Quick safety question** (integrated naturally)

2. **Quick Safety Screen**
   - "Have you had thoughts today that life might be better if you weren't here?"
   - "Do you feel safe right now?"
   - Takes 30 seconds

3. **System Response Based on Answers**
   - ✓ No concerns: Continue with anchor tracking
   - ⚠ Mild ideation: Offer expanded screen (optional)
   - 🔴 Active planning or unsafe: Activate crisis protocol

4. **If Expanded Screen Completed**
   - Risk level calculated
   - Protective factors identified
   - Next check-in scheduled
   - Anchors may adjust automatically

5. **If Crisis Detected**
   - Crisis Safe Box immediately accessible
   - Emergency contacts offered
   - 988 number displayed prominently
   - Safety planning initiated

### Assessment Examples

#### Example 1: Mild Intrusive Thoughts (Low Risk)
```
User rates ideation as "1 - Briefly, but it passed quickly"
User feels safe: Yes

System: LOW RISK
Response: "Intrusive thoughts are common, especially when tired. 
Your protective factors are strong. Continue standard anchors."
```

#### Example 2: Moderate Concern (Moderate Risk)
```
User rates ideation as "2 - Off and on"
User rates planning as "1 - Brief thoughts I dismiss"
Feeling safe: Sort of

System: MODERATE RISK
Response: "Let's build a safety plan together. Who is one person 
you could reach out to today? Your anchors are being adjusted 
to include daily connection and meaning review."
```

#### Example 3: Acute Emergency (Acute Risk)
```
User rates ideation as "4 - Almost constantly"
User rates planning as "3 - Concrete plans"
Has means access: Yes
Feeling safe: No

System: EMERGENCY PROTOCOL
Response: 🚨 IMMEDIATE ACTION NEEDED
- Call 988 or emergency services NOW
- Go to nearest emergency room
- Tell someone you trust right now
- Here are your emergency contacts: [list]
```

---

## For Users

### What Should You Know?

**This tool is meant to help you.**
- It is not perfect - it is a support, not a guarantee
- All your data is private and stays on your device
- You control when and how this is used
- You can skip any question anytime

**The goal is:**
- Early detection of patterns that need attention
- Faster access to help when you need it
- Building your safety network
- Connecting crisis support when needed

### What If I'm in Crisis Right Now?

**If you are thinking about suicide RIGHT NOW:**
1. **Call 988** (US/Canada) - Free, 24/7
2. **Go to your nearest ER**
3. **Call emergency services (911)**
4. **Tell someone you trust immediately**
5. **Do not be alone**

This app cannot replace emergency help.

### Common Questions

**Q: Will using this make me feel judged?**
A: No. The language is compassionate. We are not here to shame you.

**Q: Will this report me to police?**
A: No. We cannot report you without your knowledge, and we do not report thoughts alone. Only active emergencies get emergency services.

**Q: Is my information safe?**
A: Yes. All data is encrypted and stays on your device. We do not sell or share your data.

**Q: What if I do not want to answer these questions?**
A: You can skip any question. This tool is optional.

---

## For Clinicians

### Integration with Clinical Care

This system is designed to **complement**, not replace, your clinical assessment.

**Use this tool to:**
- Understand patterns between sessions
- Validate your clinical impression
- Provide early warning of deterioration
- Facilitate collaborative safety planning
- Document longitudinal risk assessment

**Do NOT:**
- Use as sole basis for risk determination
- Assume algorithmic score replaces clinical judgment
- Rely on it during acute crisis (clinical assessment needed)
- Substitute for direct communication

### Clinical Handoff Document

When users transfer this tool's data to you:
1. It includes all assessment responses
2. Risk level and timeline history
3. Pattern detection findings
4. Recommendations for follow-up
5. User's identified protective factors

### Suggested Clinical Workflow

```
Client in session reports increased ideation
    ↓
Ask: "What did your Polaris safety checks show this week?"
    ↓
If patterns align with assessment: Validate client's experience
    ↓
Use data to inform safety planning
    ↓
Collaborate on anchor adjustments
    ↓
Schedule increased contact if needed
    ↓
Document shared decision-making in chart
```

### Accessing User Data

Users can generate a clinical handoff document that includes:
- All assessment responses
- Risk level trajectory
- Pattern analysis
- Anchor completion data
- Recommended interventions

This is designed to be shareable with their therapist/psychiatrist.

---

## For Developers

### Installation

```javascript
import SafetyDetectionModule from './src/safety-detection.js';
import CrisisProtocol from './src/crisis-protocol.js';
import PolarisEnhancedSafety from './src/polaris-safety-integration.js';

// Initialize
const safetyModule = new SafetyDetectionModule(polarisState);
const crisisProtocol = new CrisisProtocol(userLocation);
const polarisEnhanced = new PolarisEnhancedSafety(polarisState, userLocation);
```

### Key Methods

#### Assessment
```javascript
// Quick screening
const screen = safetyModule.quickIdeationScreen();

// Evaluate responses
const riskLevel = safetyModule.calculateRiskLevel(assessmentData);

// Pattern detection
const patterns = safetyModule.detectRiskPatterns(currentState, previousState);
```

#### Crisis Response
```javascript
// Get location-specific resources
const resources = crisisProtocol.getCrisisResources({ country: 'us' });

// Generate appropriate response
const response = crisisProtocol.emergencyProtocol(userState);
const response = crisisProtocol.activeCrisisProtocol(userState, riskData);
```

#### Integration
```javascript
// Get adaptive anchors
const anchors = polarisEnhanced.generateAdaptiveAnchors(riskLevel, currentAnchors);

// Daily check-in with safety
const checkin = polarisEnhanced.dailyCheckInWithSafety();

// Determine if screening needed
const shouldScreen = polarisEnhanced.shouldAdministerExpandedScreen(state, lastDate);
```

### Configuration

Update location resources:
```javascript
// In crisis-protocol.js getCrisisResources()
const resources = {
  us: { /* US resources */ },
  ca: { /* Canada */ },
  your_country: {
    primary: [
      { name: 'Service Name', number: 'XXX-XXXX', ... }
    ]
  }
}
```

### Testing

```bash
# Run unit tests
npm test -- safety-detection.test.js

# Run integration tests
npm test -- polaris-safety-integration.test.js

# Test specific scenario
npm test -- --grep "User moves from stable to acute"
```

### Monitoring

Key metrics to track:
- Assessment completion rate
- False positive/negative rates
- Time to crisis hotline access
- User sentiment on feature
- Incident reports

See `implementation-guide.js` for detailed monitoring setup.

---

## Ethical Framework

### Core Principles

1. **Non-maleficence**: Do no harm through assessment or response
2. **Beneficence**: Active support and concrete resources
3. **Autonomy**: Respect for user choice and control
4. **Justice**: Equitable access and culturally sensitive
5. **State vs. Fate**: Current crisis is temporary, recovery is possible

### Key Commitments

✓ **Transparent language** - No shaming or stigma
✓ **Genuine resources** - All hotlines verified and active
✓ **Privacy protection** - All data encrypted, user-controlled
✓ **Cultural sensitivity** - Resources reflect diverse needs
✓ **Honest limitations** - Clear about what we cannot do
✓ **User autonomy** - Choice at every step
✓ **Continuous improvement** - Learning from outcomes

### Limitations

This system:
- Cannot guarantee safety
- Cannot replace professional care
- Cannot diagnose mental illness
- Cannot provide treatment
- Should not be used during active attempts (use 911 instead)

---

## Quick Start

### For Users
1. Open Polaris and start daily check-in
2. You'll see new safety question (integrated naturally)
3. Answer honestly - it's for your safety
4. Follow any recommendations that appear
5. If you see emergency resources, call 988 or 911

### For Clinicians
1. Ask clients if they use Polaris
2. Ask them to share assessment data in session
3. Use data to inform risk assessment
4. Collaborate on safety planning
5. Document in chart

### For Developers
1. Import the three safety modules
2. Initialize with user location
3. Add quick screen question to daily check-in
4. Implement adaptive anchor adjustment
5. Test with provided test cases
6. Monitor key metrics post-launch

---

## Support & Feedback

**User Issues?**
- Contact: support@statenotfate.com
- Crisis: Call 988 immediately

**Clinical Questions?**
- Review: [Clinician Guide]
- Contact: clinicians@statenotfate.com

**Technical Issues?**
- GitHub: [Issues & Bugs]
- Contact: dev@statenotfate.com

---

## Research & Evidence

This system builds on:
- Columbia Protocol for suicide risk assessment
- Collaborative Safety Planning (Stanley & Brown)
- Risk-Rescue Ratio (Weisman & Worden)
- Means Safety research (Swanson et al.)
- Lived experience wisdom from people with suicidality

---

## Version History

- **v2.0.0** (June 2026) - Initial Enhanced Safety Release
  - Three-tier assessment system
  - Crisis protocol integration
  - Adaptive anchor adjustment
  - Pattern detection algorithm

---

## License & Attribution

State Not Fate: Depression Recovery Operating System
Developed with consultation from:
- Suicidology experts
- People with lived suicide experience
- Mental health clinicians
- Ethicists

This work is made available to support mental health and recovery.

---

**Last Updated**: June 2026
**Maintained By**: State Not Fate Development Team
**Next Review**: January 2027

---

*State is information. Fate is a story we stop telling.*
*In crisis, reach out. Help is available. Recovery is possible.*
