interface UploadResponse {
  success: boolean;
  message: string;
  fileUrl?: string;
}

export async function uploadFile(file: File): Promise<UploadResponse> {
  const uploadURL = 'http://localhost:8000/upload';

  try {
    console.log(file);
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch(uploadURL, {
      method: 'POST',
      body: formData
    });
    console.log(response);
    const blob = await response.blob();
    console.log(blob);
    const url = URL.createObjectURL(blob);
    console.log(url);
    if (!response.ok) {
      throw new Error(response.statusText || 'Upload failed');
    }

    return {
      success: true,
      message: 'File uploaded successfully',
      fileUrl: url
    };

  } catch (error) {
    return {
      success: false,
      message: error instanceof Error ? error.message : 'Upload failed'
    };
  }
}
