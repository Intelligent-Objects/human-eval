# Commit Message Format
## Structure
```
♻️ Refactor: [System Name] [Phase/Component] [Number/Description]

[Category 1]
------------
- [Emoji] [Specific change description]
- [Emoji] [Specific change description]

[Category 2]
------------
- [Emoji] [Specific change description]
- [Emoji] [Specific change description]
```

## Example
```
♻️ Refactor: Mira Conversation System Phase 1

Test Infrastructure
------------------
- ✅ Set up pytest fixtures and mock objects
- 🔧 Configured test environment and validation
- 🧪 Added test coverage for SDK conversation features

Deprecated Files Removed
-----------------------
- 🗑️ websocket_handler.py -> SDK Conversation._run()
- 🗑️ audio_handler.py -> MiraAudioInterface  
- 🗑️ handler.py -> SDK ClientTools + ClientToolsManager
- 🗑️ handlers.py -> SDK callbacks system
- 🗑️ models.py -> SDK types + settings

Documentation
------------
- 📝 Updated success criteria in project plan
```

## Common Emojis
- ♻️ Refactor
- ✅ Completed tasks
- 🔧 Configuration
- 🧪 Testing
- 🗑️ Removals/Cleanup
- 📝 Documentation
- ⚡ Performance
- 🐛 Bug fixes
- 🔒 Security
- 🎨 UI/Style

## Guidelines
1. Group related changes under clear categories
2. Use consistent emoji prefixes
3. Keep descriptions concise but informative
4. Show clear mappings for deprecated -> new implementations
5. Include documentation updates
