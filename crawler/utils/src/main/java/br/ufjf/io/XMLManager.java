package br.ufjf.io;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.ParserConfigurationException;

import org.apache.log4j.Logger;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import org.xml.sax.SAXException;

import java.io.File;
import java.io.IOException;


public class XMLManager {

    private static Logger LOGGER = Logger.getLogger(XMLManager.class);

    private static File fXmlFile = null;
    private static DocumentBuilder dBuilder = null;
    private static Document doc = null;
    private static NodeList nList = null;

    private static final String ROOT_XML = "OBAA_Videoaula";


    private  static String removeChars(String value)
    {
        value = value.replaceAll("\n", "");
        value = value.replaceAll("                                ", " ");
        value = value.replaceAll("BEGIN:VCARD\\\\nFN:", "");
        value = value.replaceAll(":VCARD\\\\n", "");

        return value;

    }

    public static final String getValue(String property)
    {
        String result= "";

        if (nList == null) return result;

        for (int temp = 0; temp < nList.getLength(); temp++) {

            Node nNode = nList.item(temp);

            if (nNode.getNodeType() == Node.ELEMENT_NODE) {

                Element eElement = (Element) nNode;

                result = eElement.getElementsByTagName(property).item(0).getTextContent().trim();
            }
        }

        return removeChars(result);

    }



    public static final void  loadXMLFile(String filename) {
        try {

            fXmlFile = new File(filename);
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();

            dBuilder = dbFactory.newDocumentBuilder();
            doc = dBuilder.parse(fXmlFile);
            doc.getDocumentElement().normalize();
            nList = doc.getElementsByTagName(ROOT_XML);


        } catch (ParserConfigurationException e) {
            LOGGER.error("It was not possible to parse the file");
            LOGGER.error("Filename: ".concat(filename));
            e.printStackTrace();
        } catch (SAXException e) {
            LOGGER.error("It was not possible to execute SAX parse the file");
            LOGGER.error("Filename: ".concat(filename));
            e.printStackTrace();
        } catch (IOException e) {
            LOGGER.error("It was not possible to access the file");
            LOGGER.error("Filename: ".concat(filename));
            e.printStackTrace();
        }


    }

}