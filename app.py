import cv2
import numpy as np
import os

# --- CONFIGURAÇÕES ---
VIDEO_PATH = 'cat.mkv'     
OUTPUT_DIR = 'part0'
START_TIME_SEC = 1.4
END_TIME_SEC = 2.4

# --- CONFIGURAÇÕES DE RESOLUÇÃO ---
TARGET_WIDTH = 1440
TARGET_HEIGHT = 2960

# Definição do intervalo da cor verde em HSV
LOWER_GREEN = np.array([35, 100, 100])
UPPER_GREEN = np.array([85, 255, 255])
# --- FIM DAS CONFIGURAÇÕES ---

def extrair_frames_com_chroma_key():
    """
    Extrai frames de um vídeo .mkv em um intervalo de tempo específico,
    redimensiona para 1440x2960, remove o fundo verde e salva como PNGs transparentes.
    """

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Erro: Não foi possível abrir o vídeo.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        print("Erro: Não foi possível obter o FPS do vídeo.")
        fps = 30

    start_frame = int(START_TIME_SEC * fps)
    end_frame = int(END_TIME_SEC * fps)

    print(f"Vídeo com {fps:.2f} FPS. Processando do frame {start_frame} ao {end_frame}.")
    print(f"Redimensionando todos os frames para {TARGET_WIDTH}x{TARGET_HEIGHT}.")

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    
    current_frame_num = start_frame
    success_count = 0

    while current_frame_num < end_frame:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Redimensionar o frame para a resolução desejada 
        frame = cv2.resize(frame, (TARGET_WIDTH, TARGET_HEIGHT), interpolation=cv2.INTER_LINEAR)

        # --- Processo de Chroma Key ---
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, LOWER_GREEN, UPPER_GREEN)
        mask_inv = cv2.bitwise_not(mask)
        result_bgra = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        result_bgra[:, :, 3] = mask_inv
        
        # Salvar o frame processado
        output_filename = f"frame_{current_frame_num:04d}.png"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        cv2.imwrite(output_path, result_bgra)
        print(f"Salvo: {output_filename}")
        
        success_count += 1
        current_frame_num += 1

    cap.release()
    print("-" * 20)
    print(f"Processo concluído! {success_count} frames foram salvos em '{OUTPUT_DIR}'.")

if __name__ == "__main__":
    extrair_frames_com_chroma_key()