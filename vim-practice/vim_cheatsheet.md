# Level 1

-   `i` -> switch from `NORMAL` to `INSERT MODE`.
-   `x` -> delete the char which cursor located on.
-   `:wq` -> write and quit
-   `dd` -> delete whole line and copy to clipboard (cut)
-   `p` -> paste from clipboard

# Level 2

## Insert mode

-   `a` -> insert after cursor
-   `o` -> insert with newline below
-   `O` -> insert with newline above
-   `cw` -> delete current located word and start insert mode

## Cursor Move

-   `0` -> move to head of line
-   `^` -> move to first non-blank position of line
-   `$` -> move to end of line
-   `g_` -> move the the last non-blank position of line
-   `/[pattern]` -> search word with pattern

## Copy and Paste

-   `p` -> paste
-   `yy` -> copy current line

## Undo and Redo

-   `u` -> undo
-   `<C-r>` -> redo

## File Management

-   `:e <path to file>` -> open a file with path
-   `:saveas <path to file>` -> save a new file
-   `:x` `ZZ` `:wq` -> write and quit
-   `:q!` -> quit without saving
-   `:bn` `:bp` -> next tab or previous tab

# Level 3

## Repeat Command

-   `.` -> repeat last operation
-   `[N]<command>` -> repeat <command> with [N] time

## Cursor Fast Move

-   `[N]G` -> move to [N]th row
-   `gg` -> move to first row
-   `G` -> move to last row
-   `w` -> move to the head of next word
-   `e` -> move to the tail of next word
-   `%` -> go to the close/head position of brackets
-   `*` `#` -> move to next/previous matched word

# Level 4

## Cursor Fast Move

-   `f[char]` -> move to the next specific charactor
-   `t[char]` -> move to the previous position of the next specific charactor
-   `F` `T` -> same as above but with opposite direction
    > Can be used with `d`

## Section Selection

> for practice: (map (+) ("foo"))

-   `vi"` → foo.
-   `va"` → "foo".
-   `vi)` → "foo".
-   `va)` → ("foo").
-   `v2i)` → map (+) ("foo")
-   `v2a)` → (map (+) ("foo"))

## Auto-Completion

-   `<C-n>` `<C-p>` -> use in insert mode, it will show auto-completion candidates.(or just auto-complete if only one candidate)

## Macro

-   `qa` -> record your operation as `a`
-   `@a` -> replay the macro `a`
-   `@@` -> replay the last recorded macro

## Auto Function

-   `<C-a>` -> increment

## Visual Mode

-   `<C-v>` -> visual block selection
-   `J` -> concat selected line together
-   `<` `>` -> indent
-   `=` -> auto-indent
-   `A` -> enter append insert mode in Visual block mode

## Split

-   `:split` `:vsplit` -> create split tab
-   `<C-w><dir>` -> move to the tab with `<dir>`
-   `<C-w>_` `<C-w>|` -> maximize window size
-   `<C-w>+` `<C-w>-` -> increase/decrease size

## Comment

-   `gc` -> line comment
-   `gC` -> block comment
