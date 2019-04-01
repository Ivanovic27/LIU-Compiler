# LIU-Compiler
Compiler of language LIU for Compiler Design class January - May 2019
Developed with ANTLR4 and Python

# Update Lexer and Parser
```
antlr4 -Dlanguage=Python3 Liu.g4 -o ./grammar
```

# Run program
```
python main.py test.iu
```

# Commands to run GUI
````
antlr4 Liu.g4 -o ./grammar
java org.antlr.v4.Tool Liu.g4 -o ./grammar
javac ./grammar/Liu*.java
grun Liu program test.iu -gui
````
