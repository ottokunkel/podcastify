import Header from "@/components/Header";
import Features from "@/components/Features";
import FileUpload from "@/components/FileUpload";

export default function Home() {
  return (
    <main className="flex-1 container mx-auto px-4 py-12 max-w-4xl">
      <div className="flex justify-between items-center mb-8">
        <div className="flex-1">
          <Header />
        </div>
      </div>
      <div className="space-y-8">
        <FileUpload />
        <Features />
      </div>
    </main>
  );
}