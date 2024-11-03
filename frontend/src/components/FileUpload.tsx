"use client";

import { Button } from "@/components/ui/button";
import { uploadFile } from "@/tools/upload";
import { useRef, useState } from "react";

export default function FileUpload() {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [fileUrl, setFileUrl] = useState<string | null>(null);

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const response = await uploadFile(file);
      console.log(response);
      if (response.success && response.fileUrl) {
        setFileUrl(response.fileUrl);
      }
    }
  };

  return (
    <>
      {/* Upload area */}
      <div 
        className="border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg p-12 text-center"
        >
        {/* Text */}
        <p className="text-gray-600 dark:text-gray-300 mb-4">
          Drag and drop your PDF file here, or
        </p>

        {/* Button to open file input */}
        <Button onClick={() => fileInputRef.current?.click()}>
          Browse Files
          <input onChange={handleFileUpload} multiple={false} ref={fileInputRef} type='file'hidden/>
        </Button>

        <Button
          className="ml-4"
          disabled={!fileUrl}
          onClick={() => fileUrl && window.open(fileUrl, '_blank')}
        >
          Download
        </Button>

        {/* Maximum file size */}
        <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">
          Maximum file size: 10MB
        </p>
      </div>
    </>
  );
} 