/*
+--------------------------------------------------------------------------------------+
|Federal University Of Juiz de Fora - UFJF - Minas Gerais - Brazil                     |
|Institute of Hard Sciences - ICE                                                     |
|Computer Science Departament - DCC                                                    |
|Project.........: qodra - video search                                                |
|Created in......:12/12/2013                                                           |
|--------------------------------------------------------------------------------------+
*/

package br.ufjf.video;

import br.ufjf.io.FileManager;
import br.ufjf.io.XMLManager;
import br.ufjf.ontology.QodraOntology;
import org.apache.commons.lang.StringEscapeUtils;

public class Video {



    public static void main(String args[]){

        StringBuilder sb = new StringBuilder();

        XMLManager.loadXMLFile("../files/ead_fonseca_05_sd.xml");

        sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.TITLE,StringEscapeUtils.escapeJava(XMLManager.getValue("title"))));
        sb.append("\n");
        sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.ABSTRACT,StringEscapeUtils.escapeJava(XMLManager.getValue("course"))));
        sb.append("\n");
        sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.DATE,XMLManager.getValue("date")));
        sb.append("\n");
        //sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.REFERENCES,XMLManager.getValue("title")));
        //sb.append("\n");
        //sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.DESCRIPTION,XMLManager.getValue("title")));
        //sb.append("\n");
        sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.PUBLISHER,StringEscapeUtils.escapeJava(XMLManager.getValue("name"))));
        sb.append("\n");
        sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.CREATOR,StringEscapeUtils.escapeJava(XMLManager.getValue("entity"))));
        sb.append("\n");
        //sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.LICENSE,XMLManager.getValue("title")));
        //sb.append("\n");
        sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.LANGUAGE,XMLManager.getValue("language")));
        sb.append("\n");
        //sb.append(getTriple(XMLManager.getValue("entry"),QodraOntology.EDUCATIONLEVEL,XMLManager.getValue("title")));
        //sb.append("\n");


        FileManager.writeFile("../files/allegro.graph.nt",sb.toString() );

        System.out.println(sb.toString());

    }

    public static String getTriple(String subject, String predicate, String object){
        return String.format(QodraOntology.N_TRIPLE_FORMAT,subject,predicate,object);
    }
}
