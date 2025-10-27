## Reflections 
## Abhishek Rajesh Rao <br> PES2UG23CS021

Which issues were the easiest to fix, and which were the hardest? Why?

> The easiest issues to fix were stylistic issues (such as adding two blank lines between functions, removing unused imports, and renaming functions to snake_case) because these are mechanical and clearly flagged by the analysis tools. The hardest were logic and security changes (like replacing `eval`, properly handling exceptions, and fixing mutable default arguments) since these required deeper understanding of both the code’s intent and potential edge cases—making them more time-consuming and nuanced.

Did the static analysis tools report any false positives? If so, describe one example.

>Yes, static analysis tools occasionally reported missing docstrings (e.g., Pylint’s C0116 for missing function/method docstrings) as critical issues, even in trivial or extremely simple helper functions. While valuable for documentation, these do not always impact correctness or maintainability and may be deprioritized, especially in prototype or instructional code.

How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.

>Static analysis tools should be integrated into both local development and CI workflows. Locally, developers can use pre-commit hooks or run tools like Flake8, Pylint, and Bandit before pushing code. In CI, these tools can be automated to run on every pull request or commit, blocking merges if critical issues are found. This ensures code quality is consistently enforced, and errors are caught early in the development cycle.

What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

>After applying the fixes, the code is easier to read and maintain due to consistent formatting and the presence of helpful docstrings. The removal of unsafe code constructs, clearer error handling, and validation of inputs have made the codebase more robust and less likely to fail silently or be vulnerable to attacks. This results in greater confidence in the safety and maintainability of the code.