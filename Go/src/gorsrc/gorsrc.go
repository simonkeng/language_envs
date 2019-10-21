package main

import (
  "fmt"
  "log"
  "os"
  "io/ioutil"
  "github.com/urfave/cli"
)

var app = cli.NewApp()

func info() {
  app.Name = "GO Recursive SeaRCh - gorsrc"
  app.Usage = "Pass newline separated list in .txt file to gorsrc"
  app.Author = "Simon Keng"
  app.Version = "1.0.0"
}

func commands() {

  app.Flags = []cli.Flag {
    cli.StringFlag {
      Name: "list l",
      Usage: "TXT file, new line separated",
      Action: func(c *cli.Context) {
        data, err := ioutil.ReadFile("test.txt")
        if err != nil {
          fmt.Println("File reading error", err)
          return
        }
        fmt.Println(string(data))
      },
    },
  }

  app.Commands = []cli.Command {
    {
      Name: "harpie",
      Usage: "FLOOP",
      Action: func(c *cli.Context) {
        fmt.Println("BLOOP!")
      },
    },
  }

}


func main() {
  info()
  commands()

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}