# Example of ESP-IDF developing environment on Github Codespaces or VS Code Remote

<a href="https://youtu.be/md5ci_08o1E">
  <p align="center">
    <img src="./media/espidf-preview.jpg" alt="ESP-IDF developing environment on Github Codespaces" width="1024" height="782">
  </p>
</a>

- Configured ESP-IDF environment
- Install [Espressif IDF](https://marketplace.visualstudio.com/items?itemName=espressif.esp-idf-extension) and [ESP Updater extension](https://marketplace.visualstudio.com/items?itemName=masuidrive.vsc-esp-updater) for Codespaces and VS Code Rmote
- Configured [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html)

# TODOs:

- Option to skip onboarding and only generate customExtraPaths and customExtraVars? (i.e. everything is already installed in the Docker image)
- Extension: if an optional tool is installed (cmake), onboarding doesn't add it to PATH
