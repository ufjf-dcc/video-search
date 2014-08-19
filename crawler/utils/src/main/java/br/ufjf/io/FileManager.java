/*
+--------------------------------------------------------------------------------------+
|Federal University Of Juiz de Fora - UFJF - Minas Gerais - Brazil                     |
|Institute of Hard Sciences - ICE                                                     |
|Computer Science Departament - DCC                                                    |
|Project.........: qodra - video search                                                |
|Created in......:12/12/2013                                                           |
|--------------------------------------------------------------------------------------+
*/

package br.ufjf.io;


import org.apache.log4j.Logger;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class FileManager {

    private static Logger LOGGER = Logger.getLogger(FileManager.class);

    /**
     * Store a file on disk
     *
     * @param filename
     * @param content
     */
    public static final void writeFile(String filename, String content) {

        try {
            BufferedWriter out = new BufferedWriter(new FileWriter(filename));
            out.write(content);
            out.close();
        } catch (IOException e) {
            LOGGER.error("It was not possible to store the file");
            LOGGER.error("Filename: ".concat(filename));
            LOGGER.error("Content: ".concat(content));
            e.printStackTrace();
        }

    }


}
