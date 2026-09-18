# LeetCode Workspace Manager

A local CLI that pulls a LeetCode problem via GraphQL, writes a Markdown
problem statement and a runnable Python template, opens both in VS Code,
and logs your solve time/status to a CSV when you're done.

## Where to put this on your machine

Your `DSA` folder already has category subfolders (`Leetcode Problems`,
`Striver Sheet`, `GFG`, ...). Keep this tool in its own subfolder so it
doesn't mix with your solved files:

```
C:\Users\Pranesh\Downloads\VS CODE\DSA\
├── read.md                     <- already exists, gets overwritten each run
├── Leetcode Problems\          <- already exists, new <id>.py files land here
├── leetcode-workspace\         <- put this tool here (new folder)
│   ├── lc.py
│   ├── finish.py
│   ├── requirements.txt
│   ├── config.json             <- auto-created on first run
│   ├── session.json            <- auto-created/deleted per session
│   ├── leetcode_log.csv        <- auto-created on first finish
│   └── core\
│       └── ...
```

### Steps

1. Unzip this project so it becomes:
   `C:\Users\Pranesh\Downloads\VS CODE\DSA\leetcode-workspace\`
2. Open a terminal in that new folder.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Make sure the VS Code `code` command is on PATH (in VS Code:
   Ctrl+Shift+P -> "Shell Command: Install 'code' command in PATH").
5. Run it:
   ```
   python lc.py
   ```
   On first run it will ask you to confirm the paths in `config.json` --
   the defaults already point at your `Leetcode Problems` folder and
   `read.md`, so you can just press Enter through each prompt.

## Daily use

```
python lc.py       # enter a problem number -> generates read.md + <id>.py,
                    # opens both in VS Code, starts a session
... solve it ...
python finish.py    # asks Status + Notes, computes elapsed time automatically,
                    # appends a row to leetcode_log.csv, deletes session.json
```

## Config (`config.json`, auto-created on first run)

| Key                     | Meaning                                            |
|-------------------------|-----------------------------------------------------|
| `leetcode_folder`       | Where `<id>.py` files are written (`Leetcode Problems`) |
| `markdown_file`         | The single file that gets overwritten each run (`read.md`) |
| `csv_log`               | Solve history CSV                                  |
| `vscode_project_folder` | Folder VS Code opens (`DSA`)                        |
| `session_file`          | Tracks the one active session                       |
| `auto_open_vscode`      | Set `false` to skip opening VS Code automatically   |
| `auto_split_editor`     | Set `false` to skip the split-editor tip message    |

You can edit `config.json` by hand at any time -- delete it to re-run the
first-time setup prompts.

## Known limitations (by design, kept simple on purpose)

- **VS Code split view**: the `code` CLI can't force a true split layout.
  Both files open as tabs in the same group; pressing `Ctrl+\` once splits
  them, and VS Code remembers that layout for next time. A keystroke-automation
  workaround was deliberately left out -- it's fragile and depends on window
  focus timing, which isn't worth the complexity for a one-time action per day.
- **Sample runner / pytest args**: LeetCode's example input (e.g.
  `nums = [2,7,11,15], target = 9`) is inserted into the commented call as-is
  for readability. It may need light manual edits before uncommenting and running.
- **Premium problems**: skipped with a clear message, no workaround attempted.
- **Problem list lookup**: resolving a problem number requires paginating
  LeetCode's question list; very high problem numbers may take a few seconds.
