import re
from Bio import Medline
import pandas as pd
from tqdm import tqdm
import logging

# Configurar logger
logger = logging.getLogger(__name__)

class PubMedParser:
    """
    Procesa archivos .nbib de PubMed y extrae información relevante para revisiones sistemáticas.
    """
    
    def __init__(self):
        self.doi_pattern = re.compile(r'(10\.\S+)\s*\[doi\]')
        logger.info("PubMedParser inicializado")
    
    def extract_doi(self, lid_value: str) -> str:
        """Extrae DOI de campo LID usando expresión regular"""
        if not lid_value:
            return ""
        
        match = self.doi_pattern.search(lid_value)
        return match.group(1) if match else ""
    
    def process_pubmed_nbib(self, input_file: str, output_file: str) -> pd.DataFrame:
        """
        Procesa un archivo .nbib de PubMed y guarda los datos en CSV.
        
        Args:
            input_file: Ruta al archivo .nbib
            output_file: Ruta al archivo CSV de salida
            
        Returns:
            DataFrame con los artículos procesados
        """
        logger.info(f" Procesando archivo: {input_file}")
        
        try:
            # Leer el archivo
            with open(input_file, 'r', encoding='utf-8') as handle:
                records = list(Medline.parse(handle))
            
            logger.info(f" Encontrados {len(records)} artículos en el archivo")
            
            # Procesar cada registro
            data = []
            for record in tqdm(records, desc=" Procesando artículos"):
                # Extraer campos básicos
                pmid = record.get("PMID", "")
                title = record.get("TI", "").strip()
                abstract = record.get("AB", "").strip()
                authors = ", ".join(record.get("AU", []))
                journal = record.get("JT", "").strip()
                
                # Extraer año
                dp_value = record.get("DP", "")
                year_match = re.search(r'(\d{4})', dp_value)
                year = year_match.group(1) if year_match else ""
                
                # Extraer DOI
                lid_value = record.get("LID", "")
                doi = self.extract_doi(lid_value)
                
                # Extraer keywords
                keywords = ", ".join(record.get("OT", [])) if "OT" in record else ""
                
                # Determinar tipo de publicación
                pub_types = record.get("PT", [])
                publication_type = "; ".join(pub_types)
                is_journal_article = "Journal Article" in publication_type
                
                # Verificar si está retractado
                title_lower = title.lower()
                pub_types_lower = [pt.lower() for pt in pub_types]
                retracted_keywords = ['retract', 'withdrawn', 'correction notice']
                retracted_types = ['retracted publication', 'retraction of publication']
                
                retracted = (any(keyword in title_lower for keyword in retracted_keywords) or
                           any(rtype in pub_types_lower for rtype in retracted_types))
                
                data.append({
                    "PMID": pmid,
                    "Title": title,
                    "Abstract": abstract,
                    "Authors": authors,
                    "Year": year,
                    "Journal": journal,
                    "DOI": doi,
                    "Keywords": keywords,
                    "PublicationType": publication_type,
                    "IsJournalArticle": is_journal_article,
                    "Retracted": retracted,
                    "Database": "PubMed"
                })
            
            # Crear DataFrame
            df = pd.DataFrame(data)
            
            # Guardar CSV
            df.to_csv(output_file, index=False)
            logger.info(f" Archivo guardado como: {output_file}")
            logger.info(f" Total de artículos procesados: {len(df)}")
            
            return df
            
        except Exception as e:
            logger.error(f" Error procesando el archivo: {str(e)}")
            raise

def process_pubmed_nbib(input_file: str, output_file: str) -> pd.DataFrame:
    """
    Función wrapper para facilitar el uso desde scripts.
    """
    parser = PubMedParser()
    return parser.process_pubmed_nbib(input_file, output_file)