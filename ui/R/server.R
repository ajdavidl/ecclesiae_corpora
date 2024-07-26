library(shiny)
library(shinydashboard)


shinyServer(function(input, output) {
  output$textEvangPapaeVerba <- renderText({ 
    print(input$selectInputPapaeVerba)
    pt[[input$selectInputPapaeVerba]]$evangelho
    })
  output$textHomPapaeVerba <- renderUI({ 
    print(input$selectInputPapaeVerba)
    homilias <- pt[[input$selectInputPapaeVerba]]$homilias
    if(length(homilias) == 1){
      return(homilias)
    }else{
      paste(homilias, collapse = "<br>")
    }
    })
})