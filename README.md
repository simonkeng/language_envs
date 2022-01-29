# Language Envs

Minimal containers for trying out new programming languages, intended for my learning, but may be useful for prototyping. The environments are containerized to be easily deployed, and provides a  replicable runtime environment for collaboration sanity and application consistency.

- Assembly
- C ✅
- C++ ✅
- Clojure ✅
- Elixir
- Fortran
- Go ✅
- Haskell
- Java
- JavaScript ✅
- Kotlin
- Lisp
- Lua ✅
- Python ✅
- Ruby
- Rust ✅
- Scala ✅
- Swift
- TypeScript ✅


### Project ideas:

- Containerize programs with interesting polyglot mixtures.
- Interface two or more languages (e.g. swig for Python --> C++).
- Language layering, low-level to high (e.g. JS frontend that calls a Ruby backend, and uses C interface for low-level system call, then float data back up to the top).
- Connect containers over docker network and send data between different languages (e.g. restful API between NodeJS web app and a Go/Rust web server)
- Docker composify (or k8s) to have 4 or more containers sending and receiving data between them, passing data between languages.

