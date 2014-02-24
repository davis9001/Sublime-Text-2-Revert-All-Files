Sublime-Text-Revert-All-Files
===============================

Plugin for Sublime Text 2/3 adding a window command to revert all unsaved files to their last saved state.

# Revert All Files

Have you ever done a search-and-replace on an entire large project, only to then realize that you made an irreversable mistake? That happened to me recently and I was shocked to find that Sublime Text 2 did not have a Replace All Files command (at least not that I could find).

This plugin adds the command ('revert_all') and a handy menu item in the File menu. This command will first open a confirmation dialog making sure you REALLY want to revert and undo all unsaved changes (because it could be a big pain to restore them again)...

The command has not yet been given a keyboard shortcut, you can always add this in your User preferences if you want; if everyone seems to want this though I'll be happy to add it. Or if you're feeling froggy, jump on in by forking the repo and sending a pull request with your patch! :)
