import { ArrowRight } from 'lucide-react';

const links = [
  { label: 'Product', href: '#product' },
  { label: 'How it works', href: '#how-it-works' },
  { label: 'Why FORGE', href: '#why-forge' },
];

interface FooterProps {
  onEnterForge?: () => void;
}

export default function Footer({ onEnterForge }: FooterProps = {}) {
  return (
    <footer className="border-t border-foreground/[0.08] bg-background px-6 py-14 sm:px-8 sm:py-16 lg:px-12">
      <div className="mx-auto flex max-w-7xl flex-col gap-10 sm:flex-row sm:items-start sm:justify-between">
        {/* Brand */}
        <div>
          <a
            href="#top"
            className="font-display text-xl tracking-tight text-foreground"
          >
            FORGE
          </a>
        </div>

        {/* Navigation */}
        <nav className="flex flex-wrap gap-x-8 gap-y-3">
          {links.map((l) => (
            <a
              key={l.label}
              href={l.href}
              className="text-[0.88rem] text-foreground-soft transition-colors duration-200 hover:text-foreground"
            >
              {l.label}
            </a>
          ))}
          <a
            href="#enter"
            onClick={(e) => {
              if (onEnterForge) {
                e.preventDefault();
                onEnterForge();
              }
            }}
            className="inline-flex items-center gap-1.5 text-[0.88rem] text-foreground transition-colors duration-200 hover:text-accent"
          >
            Enter FORGE
            <ArrowRight className="h-3 w-3" />
          </a>
        </nav>
      </div>

      {/* Copyright */}
      <div className="mx-auto mt-10 max-w-7xl border-t border-foreground/[0.06] pt-6">
        <p className="text-[0.75rem] text-foreground-faint">
          © {new Date().getFullYear()} FORGE. All rights reserved.
        </p>
      </div>
    </footer>
  );
}
