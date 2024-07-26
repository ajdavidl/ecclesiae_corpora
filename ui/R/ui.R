library(shiny)
library(shinydashboard)
library(shinycssloaders)
library(rjson)

pt <- fromJSON(file = "../../papae_verba/pt.json")

citations <- sort(names(pt))

header <- dashboardHeader(
  title = "Ecclesiae corpora",
  titleWidth = 450
)

sidebar <- dashboardSidebar(
  width = 380,
  
  
  h3(" Menu"),
  sidebarMenu(
    id = "menuItens",
    menuItem("Papae Verba", tabName = "papae_verba", icon = icon("file"))#,
    #menuItem("??", tabName = "xx", icon = icon("file-archive"))
  )
)

body <- dashboardBody(
  tags$head(tags$style(HTML('
      .main-header .logo {
        font-family: "Georgia", Times, "Times New Roman", serif;
        font-weight: bold;
        font-size: 24px;
      }
    '))),
  tabItems(
    tabItem(
      tabName = "papae_verba",
      fluidRow(
        column(
          width = 5,
          box(
            title = "Itens:",
            selectInput("selectInputPapaeVerba","citations:", citations)
        )
      )),
      fluidRow(
        box(textOutput("textEvangPapaeVerba"),),
        #box(textOutput("textHomPapaeVerba"),)
        box(htmlOutput("textHomPapaeVerba"),)
      
    )#,
    #tabItem()
)
)
)

dashboardPage(header, sidebar, body, skin="black")