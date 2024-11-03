export default function Features() {
  const features = [
    "Natural voice synthesis",
    "Multiple language support",
    "Adjustable reading speed",
    "Download MP3 files",
  ];

  return (
    <div className="mt-8">
      <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
        Features
      </h2>
      <ul className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {features.map((feature, index) => (
          <li key={index} className="flex items-center space-x-3 text-gray-600 dark:text-gray-300">
            <svg className="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
              <path
                fillRule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clipRule="evenodd"
              />
            </svg>
            <span>{feature}</span>
          </li>
        ))}
      </ul>
    </div>
  );
} 